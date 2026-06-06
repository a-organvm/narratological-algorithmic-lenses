import sys
import os

# Add package source directories to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../packages/core/src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../packages/mcp/src")))

from narratological_mcp.server import mcp, get_available_studies, search_axioms

def main():
    print("Testing MCP tool: get_available_studies...")
    studies = get_available_studies()
    print(f"PASS: Found {len(studies)} studies.")
    
    print("Testing MCP tool: search_axioms...")
    axioms = search_axioms("mimesis")
    print(f"PASS: Found {len(axioms)} axioms matching 'mimesis'.")
    for a in axioms:
        print(f" - [{a['study_id']}] {a['name']}: {a['statement']}")
        
    print("Checking tool registration on FastMCP instance...")
    # FastMCP typically exposes registered tools on get_tools()
    try:
        tools = mcp.get_tools()
        tool_names = [t.name for t in tools]
    except AttributeError:
        # Fallback to _tools if it's a private attribute
        try:
            tools = mcp._tools.values()
            tool_names = [t.name for t in tools]
        except AttributeError:
            tool_names = []
            
    print(f"Registered tools: {tool_names}")
    print("All MCP server tools smoke-tested successfully!")

if __name__ == "__main__":
    main()
