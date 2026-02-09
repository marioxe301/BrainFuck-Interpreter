const codeInput = document.getElementById("code-input");
const stdinInput = document.getElementById("stdin-input");
const runButton = document.getElementById("run-code");
const outputBox = document.getElementById("output-box");
const errorBox = document.getElementById("error-box");
const loadSampleButton = document.getElementById("load-sample");
const clearButton = document.getElementById("clear-code");
const statusIndicator = document.getElementById("status-indicator");

const sampleCode =
  "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.";

const setStatus = (status) => {
  statusIndicator.textContent = status;
};

const setError = (message) => {
  if (message) {
    errorBox.textContent = message;
    errorBox.classList.remove("hidden");
  } else {
    errorBox.textContent = "";
    errorBox.classList.add("hidden");
  }
};

const setOutput = (text) => {
  outputBox.textContent = text || "";
};

const runCode = async () => {
  const code = codeInput.value;
  const input = stdinInput.value;

  if (!code.trim()) {
    setError("Please paste Brainfuck code to run.");
    return;
  }

  setError("");
  setStatus("Running");
  runButton.disabled = true;
  runButton.classList.add("opacity-70");

  try {
    const response = await fetch("/api/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, input }),
    });

    const payload = await response.json();
    if (!response.ok || !payload.success) {
      setOutput("");
      setError(payload.error || "Execution failed.");
      return;
    }

    setOutput(payload.output || "(no output)");
  } catch (error) {
    setOutput("");
    setError("Server unreachable. Start the Python server first.");
  } finally {
    setStatus("Idle");
    runButton.disabled = false;
    runButton.classList.remove("opacity-70");
  }
};

runButton.addEventListener("click", runCode);

codeInput.addEventListener("keydown", (event) => {
  if (event.ctrlKey && event.key === "Enter") {
    runCode();
  }
});

loadSampleButton.addEventListener("click", () => {
  codeInput.value = sampleCode;
  setOutput("");
  setError("");
});

clearButton.addEventListener("click", () => {
  codeInput.value = "";
  setOutput("Output will appear here.");
  setError("");
});
