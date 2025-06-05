#!/usr/bin/env python3
"""One-click installer and launcher for MCP Feedback Collector."""

import subprocess
import sys
from pathlib import Path


def run_cmd(cmd):
    """Run a command and raise if it fails."""
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


def main():
    base_dir = Path(__file__).resolve().parent
    requirements = base_dir / "requirements.txt"

    # Install dependencies from requirements.txt if present
    if requirements.exists():
        run_cmd([sys.executable, "-m", "pip", "install", "-r", str(requirements)])

    # Install the package itself in editable mode
    run_cmd([sys.executable, "-m", "pip", "install", "-e", str(base_dir)])

    # Launch the feedback collector server
    run_cmd([sys.executable, "-m", "mcp_feedback_collector.server"])


if __name__ == "__main__":
    main()
