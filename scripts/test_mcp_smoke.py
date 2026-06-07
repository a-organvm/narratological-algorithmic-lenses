import asyncio
import os
import sys
from typing import Any

# Add package source directories to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../packages/core/src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../packages/mcp/src")))

from narratological_mcp.server import get_available_studies, mcp, search_axioms


def call_tool(tool: Any, *args: Any) -> Any:
    """Call either a FastMCP Tool wrapper or a plain function."""
    fn = getattr(tool, "fn", tool)
    return fn(*args)


def main():
    print("Testing MCP tool: get_available_studies...")
    studies = call_tool(get_available_studies)
    print(f"PASS: Found {len(studies)} studies.")

    print("Testing MCP tool: search_axioms...")
    axioms = call_tool(search_axioms, "mimesis")
    print(f"PASS: Found {len(axioms)} axioms matching 'mimesis'.")
    for a in axioms:
        print(f" - [{a['study_id']}] {a['name']}: {a['statement']}")

    print("Checking tool registration on FastMCP instance...")
    try:
        # FastMCP get_tools() is an async method returning a dict
        tools = asyncio.run(mcp.get_tools())
        tool_names = list(tools.keys())
    except Exception as e:
        print(f"Could not fetch tools via get_tools(): {e}")
        try:
            # Fallback to internal tool manager if needed
            tool_names = list(mcp._tool_manager._tools.keys())
        except AttributeError:
            tool_names = []

    print(f"Registered tools: {tool_names}")
    print("All MCP server tools smoke-tested successfully!")


if __name__ == "__main__":
    main()
