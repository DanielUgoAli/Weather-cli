#!/usr/bin/env bash

# Function to print error messages in red
error() {
    echo -e "\e[31m$1\e[0m"
}

# Function to print success messages in green
success() {
    echo -e "\e[32m$1\e[0m"
}

# Locate the project root (Weather-CLI)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Navigate to project root
cd "$PROJECT_ROOT" || { error "Failed to locate project root."; exit 1; }

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    error "Python3 is not installed. Please install it and try again."
    exit 1
fi

# Check if virtual environment exists
if [ -d "$PROJECT_ROOT/.venv" ]; then
    success "Activating virtual environment..."
    source "$PROJECT_ROOT/.venv/bin/activate"
elif [ -f "$PROJECT_ROOT/requirements.txt" ]; then
    error "Virtual environment not found. Creating one..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    error "No virtual environment or requirements.txt found. Exiting..."
    exit 1
fi

# Navigate to src directory
cd "$PROJECT_ROOT/src" || { error "Failed to change directory to src."; exit 1; }

# Check if cli.py exists
if [ ! -f "cli.py" ]; then
    error "Error: cli.py not found in src directory."
    exit 1
fi

# Run cli.py using Python3
success "Running cli.py..."
python3 -u cli.py
