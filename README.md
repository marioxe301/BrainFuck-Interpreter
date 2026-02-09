# Brainfuck Interpreter
Simple Brainfuck parser and interpreter in Python, plus a small web runner UI.

## Features
- CLI interpreter with syntax validation.
- Web UI to run Brainfuck via the Python server.
- uv-based dependency management.
- Dockerfile and compose workflow.

## Installation

### Using uv (recommended)
```bash
uv sync
```

## Quick Start

### CLI
```bash
python main.py path/to/program.bf
```

With uv:
```bash
uv run python main.py path/to/program.bf
```

### Web UI (single service)
```bash
python server.py --host 127.0.0.1 --port 8000
```
Then open `http://127.0.0.1:8000`.

### Web UI (separate services)
```bash
python server.py --api-only --host 127.0.0.1 --port 8000
python -m http.server 5173 -d web
```
Then open `http://127.0.0.1:5173`.

## Usage

### Brainfuck commands
| Operator | Description |
|:--:|:--|
| `+` | Add 1 to the current cell |
| `-` | Subtract 1 from the current cell |
| `>` | Move pointer right |
| `<` | Move pointer left |
| `.` | Output ASCII character at pointer |
| `,` | Read one character of input into current cell |
| `[` | Start loop |
| `]` | End loop |

### API
`POST /api/run`

Request:
```json
{ "code": "++++[>++++<-]>", "input": "" }
```

Response:
```json
{ "success": true, "output": "A" }
```

Errors:
- `400` invalid input
- `422` invalid Brainfuck syntax

### Input behavior
If the program reads more input than provided, the server supplies a null byte (`\x00`).

## Docker

### Build and run
```bash
docker build -t brainfuck .
docker run -p 8000:8000 brainfuck
```

### Docker Compose
```bash
docker compose up --build
```

Split services (API + static web):
```bash
docker compose --profile split up --build
```

## Development Notes
- Interpreter entrypoint: `main.py`.
- Web server entrypoint: `server.py`.
- Frontend assets: `web/`.

## License
MIT
