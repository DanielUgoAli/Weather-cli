#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed."
    if [ -x "$(command -v apt)" ]; then
        echo "Installing Python3 using apt..."
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif [ -x "$(command -v yum)" ]; then
        echo "Installing Python3 using yum..."
        sudo yum install -y python3
    elif [ -x "$(command -v brew)" ]; then
        echo "Installing Python3 using Homebrew..."
        brew install python3
    else
        echo "Please install Python3 manually and try again."
        exit 1
    fi
fi

# Find the repository root using Git
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
if [ -z "$REPO_ROOT" ]; then
    echo "This script must be run from within the repository."
    exit 1
fi

# Run cli.py from the repository root
cd "$REPO_ROOT/src" || { echo "Failed to change directory."; exit 1; }
python3 -u cli.py
