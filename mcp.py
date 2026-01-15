import os
import subprocess
import sys

# Path to the actual mcp.py script relative to the project root
MCP_PATH = os.path.join("mcp-global", "mcp-global-rules", "mcp.py")

def main():
    if not os.path.exists(MCP_PATH):
        print(f"Error: Could not find mcp-global rules at {MCP_PATH}")
        sys.exit(1)

    # Proxy all arguments to the actual script
    cmd = [sys.executable, MCP_PATH] + sys.argv[1:]

    try:
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"Error running mcp.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
