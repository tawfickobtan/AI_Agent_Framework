# Agent Framework

A lightweight Python agent framework for experimenting with tool-enabled LLM workflows.

This repo contains small building blocks to:
- Define an LLM model wrapper (`Model`)
- Define tools with JSON schema (`Tool`)
- Build an agent that sends messages + tool schemas to a chat completion model (`Agent`)

## Project Structure

- `agent.py` – Agent class, tool registry setup, and single-step model call.
- `model.py` – OpenAI-compatible chat completion wrapper.
- `tool.py` – Current `Tool` class (minimal/incomplete implementation).
- `tool copy.py` – Alternate `Tool` implementation with decorator + schema support.
- `test.py` – Example usage (tool declaration, model call, and agent step).

## Requirements

- Python 3.10+
- Packages:
  - `openai`
  - `python-dotenv`
- API key for an OpenAI-compatible endpoint (example in this repo uses Groq API compatibility).

## Installation

```bash
pip install openai python-dotenv
```

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## Quick Start

Run the example:

```bash
python test.py
```

## How It Works

1. A tool is defined with a name, description, and JSON input schema.
2. `Agent` collects all tool schemas and sends them in `tools` to the model.
3. `Model.complete()` calls chat completions with `tool_choice="auto"`.
4. `Agent.step()` returns the model message for the current conversation state.

## Important Note

`test.py` currently uses `@Tool.toolthis(...)`, which is implemented in `tool copy.py`, but **not** in the active `tool.py`.

If you run into errors, either:
- Replace `tool.py` with the implementation from `tool copy.py`, or
- Update `test.py` to match the current `Tool` class in `tool.py`.

## Example: Current Agent Loop

Minimal flow in this repo:

```python
agent.add_message(role="user", content="What is 5 + 7?")
response = agent.step()
print(response)
```

## Next Improvements

- Add full tool-call execution loop (parse tool calls, execute Python function, append tool result, continue).
- Unify `tool.py` and `tool copy.py` into one canonical implementation.
- Add tests for tool registration and duplicate handling.
- Add type hints + validation for tool schemas.

## License

No license file is currently included. Add a `LICENSE` file before publishing if needed.
"# AI_Agent_Framework" 
