import subprocess
from pathlib import Path
import json

def run_mcp_command(command: str, target: str = ".") -> str:
    """Runs an mcp-global command via the root proxy and returns output."""
    try:
        # Using the project root's mcp.py proxy
        result = subprocess.run(
            ["python", "mcp.py", command, target],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        return result.stdout
    except Exception as e:
        return f"Error running mcp {command}: {str(e)}"

def generate_ai_feedback_report():
    """Aggregates mcp-global findings into AI_FEEDBACK.md."""
    print("--- Generating AI Feedback Report ---")
    
    # Run core analysis tools
    review_output = run_mcp_command("review", "backend/")
    security_output = run_mcp_command("security", "backend/")
    # You could add others like 'errors' or 'predict-bugs'
    
    report_content = [
        "# AI Agent Feedback Report",
        f"Generated: {subprocess.check_output(['git', 'log', '-1', '--format=%ai']).decode().strip()}",
        "",
        "## 🔍 Code Review Findings",
        "```text",
        review_output,
        "```",
        "",
        "## 🛡️ Security Audit",
        "```text",
        security_output,
        "```",
        "",
        "## 💡 Action Items for AI Agents",
        "Based on the findings above, please prioritize fixing the identified warnings and errors in the next session.",
        "Always check this file after `autocontext` to stay informed about codebase health."
    ]
    
    report_path = Path.cwd() / "AI_FEEDBACK.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_content))
    
    print(f"   Success: AI_FEEDBACK.md updated.")
    return report_path

if __name__ == "__main__":
    generate_ai_feedback_report()
