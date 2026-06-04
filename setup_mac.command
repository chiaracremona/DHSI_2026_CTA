#!/bin/bash
# Double-click this file to set up the project: install Python and all
# required libraries. After it finishes, open the .ipynb file in VS Code.

set -e
cd "$(dirname "$0")"

# Install uv if it isn't already on PATH or in the standard install location.
if ! command -v uv &> /dev/null; then
    if [ ! -x "$HOME/.local/bin/uv" ]; then
        echo "Installing uv (one-time setup) ..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
    fi
    export PATH="$HOME/.local/bin:$PATH"
fi

echo "Installing dependencies ..."
uv sync

echo
echo "Setup complete. Open the notebook (.ipynb file) in VS Code."
echo "When VS Code asks which Python interpreter to use, choose:"
echo "  $(pwd)/.venv/bin/python"
echo
read -p "Press Enter to close this window."
