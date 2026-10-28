from mcp.server.fastmcp import FastMCP


mcp = FastMCP("asgi-demo")


@mcp.tool()
def greet(name: str) -> str:
    """Return a greeting for a name."""
    return f"Hello, {name}!"
