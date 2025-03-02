# Check if Python is installed (either python or py)
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} else {
    Write-Host "Python is not installed. Please install Python and try again."
    exit 1
}


# Find the repository root using Git
$REPO_ROOT = git rev-parse --show-toplevel 2>$null
if (-not $REPO_ROOT) {
    Write-Host "This script must be run from within the repository."
    exit 1
}

# Navigate to the src directory and run cli.py
Set-Location -Path "$REPO_ROOT\src"
& $pythonCmd cli.py
