# ASGI MCP Demo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a minimal ASGI application that mounts an MCP server at `/mcp` without LangChain or Django.

**Architecture:** `server.py` owns the `FastMCP` instance and one tool. `asgi.py` exposes the MCP app at `/mcp` and handles `/health` plus unknown HTTP paths directly. The demo is started with Uvicorn.

**Tech Stack:** Python 3.11+, `mcp>=1,<2`, Starlette via the MCP SDK, Uvicorn.

**Spec:** `docs/superpowers/specs/2026-10-28-asgi-mcp-demo-design.md`

## Global Constraints

- Do not use LangChain, Django, or a model API.
- Do not modify the existing stdio/SSE demos.
- Keep the example intentionally small; no authentication, database, or production middleware.

## Review Focus

- `GET /health` must remain available outside the MCP route.
- `/mcp` must expose the tool through the MCP streamable HTTP transport.
- Unknown paths must return a normal 404 response rather than being sent to MCP.
- The server module must be importable without starting a listener.

### Task 1: Add the ASGI MCP server module

**Files:**
- Create: `demo/asgi_mcp/__init__.py`
- Create: `demo/asgi_mcp/server.py`
- Create: `demo/asgi_mcp/asgi.py`

**Interfaces:**
- Produces `demo.asgi_mcp.server.mcp: FastMCP`.
- Produces `demo.asgi_mcp.asgi.application: ASGI callable`.

- [ ] **Step 1: Add the `FastMCP` server and one deterministic tool**

  Define `mcp = FastMCP("asgi-demo")` and a `greet(name: str) -> str` tool returning a deterministic greeting. Do not call `mcp.run()` on import.

- [ ] **Step 2: Compose the ASGI application**

  Build `mcp_app = mcp.streamable_http_app()` and route only `/mcp` and `/mcp/*` to it. Return `{"status": "ok"}` from `/health`, and return 404 for other paths.

- [ ] **Step 3: Add the package marker**

  Add an empty `__init__.py` so the module can be started with `uvicorn demo.asgi_mcp.asgi:application`.

### Task 2: Document and wire the runnable demo

**Files:**
- Modify: `requirements.txt`
- Create: `demo/asgi_mcp/README.md`

**Interfaces:**
- The documented command starts `demo.asgi_mcp.asgi:application` on port 8000.

- [ ] **Step 1: Add the minimal runtime dependency**

  Add `uvicorn` to `requirements.txt` only if it is not already provided by the existing dependency set; keep the existing dependency constraints unchanged.

- [ ] **Step 2: Document startup and routes**

  Explain installation, `uvicorn demo.asgi_mcp.asgi:application --reload`, `GET /health`, and how to use MCP Inspector against `http://127.0.0.1:8000/mcp`.

### Task 3: Verify behavior

**Files:**
- Test: `demo/asgi_mcp/test_asgi.py`

- [ ] **Step 1: Add focused ASGI tests**

  Use an ASGI test client or direct ASGI calls to assert `/health` returns 200 and the expected JSON, unknown paths return 404, and the module exposes `application` without starting a server.

- [ ] **Step 2: Run the focused tests**

  Run `pytest demo/asgi_mcp/test_asgi.py -q` and expect all tests to pass.

- [ ] **Step 3: Run the existing stdio contract script**

  Run `python demo/stdio/test_contract.py` and expect it to complete without an assertion failure, confirming the new demo did not alter the existing MCP server.
