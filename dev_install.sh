#!/bin/bash

# Detect the OS
OS="$(uname)"

if [ "$OS" = "Darwin" ]; then
    # If the OS is macOS, proceed with the installation
    echo "Detected macOS. Running Nuitka to create a standalone executable."

    # Install nuitka if not already installed
    if ! [ -x "$(command -v uv)" ]; then
        echo "uv not found. Please install uv before running this script."
        exit 1
    fi

    # Run nuitka to create a standalone executable
    uv run python -m nuitka --standalone --onefile src/fob/__init__.py --output-filename=fob

    DEST_PATH="$HOME/.local/bin"

    # Delete previous version
    rm "$DEST_PATH/fob"

    # Copy the executable to somewhere on your PATH
    echo "Copying the executable to $DEST_PATH..."
    mkdir -p "$DEST_PATH"
    cp fob "$DEST_PATH"

    # Clean up
    echo "Cleaning up..."
    rm -r __init__.dist __init__.build __init__.onefile-build

    echo "Installation complete. The 'fob' command is now available. If not, please check that $DEST_PATH is in your PATH environment variable."
else
    # Print a message for unsupported OS
    echo "The installation script is not implemented for $OS."
fi
