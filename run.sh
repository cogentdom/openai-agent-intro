#!/bin/bash
# Helper script to run Python files with the correct Python version

echo "Running with Python 3.9 (required for openai-agents package)..."

if command -v python3.9 &> /dev/null; then
    python3.9 "$@"
else
    echo "Error: Python 3.9 not found. Please install Python 3.9 or higher."
    echo "The openai-agents package requires Python 3.9+."
    exit 1
fi
