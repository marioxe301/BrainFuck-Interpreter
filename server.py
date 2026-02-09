import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

from runner import run_code


def json_response(handler, status, payload):
    data = json.dumps(payload).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def read_request_json(handler):
    length = int(handler.headers.get("Content-Length", "0"))
    if length <= 0:
        return {}
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))


def safe_static_path(static_root, request_path):
    normalized = unquote(request_path.split("?", 1)[0]).lstrip("/")
    if normalized == "":
        normalized = "index.html"
    target = (static_root / normalized).resolve()
    if not str(target).startswith(str(static_root)):
        return None
    if target.is_dir():
        target = target / "index.html"
    return target


def guess_content_type(path):
    if path.suffix == ".html":
        return "text/html; charset=utf-8"
    if path.suffix == ".js":
        return "text/javascript; charset=utf-8"
    if path.suffix == ".css":
        return "text/css; charset=utf-8"
    if path.suffix == ".svg":
        return "image/svg+xml"
    return "application/octet-stream"


class BrainfuckHandler(BaseHTTPRequestHandler):
    server_version = "BrainfuckHTTP/1.0"

    def do_POST(self):
        if self.path != "/api/run":
            json_response(self, 404, {"error": "Not found"})
            return

        try:
            payload = read_request_json(self)
        except json.JSONDecodeError:
            json_response(self, 400, {"error": "Invalid JSON"})
            return

        code_text = payload.get("code", "")
        input_text = payload.get("input", "")

        if not isinstance(code_text, str) or code_text.strip() == "":
            json_response(self, 400, {"error": "Code is required"})
            return

        if not isinstance(input_text, str):
            json_response(self, 400, {"error": "Input must be a string"})
            return

        result = run_code(code_text, input_text)
        status = 200 if result.get("success") else 422
        json_response(self, status, result)

    def do_GET(self):
        if self.server.api_only:
            json_response(self, 404, {"error": "Not found"})
            return

        target = safe_static_path(self.server.static_root, self.path)
        if not target or not target.exists():
            self.send_response(404)
            self.end_headers()
            return

        data = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", guess_content_type(target))
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format, *args):
        return


def main():
    parser = argparse.ArgumentParser(description="Brainfuck web runner")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--api-only", action="store_true")
    parser.add_argument("--static-dir", default="web")
    args = parser.parse_args()

    static_root = Path(args.static_dir).resolve()
    server = ThreadingHTTPServer((args.host, args.port), BrainfuckHandler)
    server.static_root = static_root
    server.api_only = args.api_only
    server.serve_forever()


if __name__ == "__main__":
    main()
