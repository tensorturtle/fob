![banner](/assets/banner.png)

# `fob`
[![Build & Test](https://github.com/tensorturtle/fob/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/tensorturtle/fob/actions/workflows/tests.yaml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**Focus Blocks** is my take on time management inspired by Flow State, Pomodoro Technique, Timeboxing, and Deep Work. Please read the [Introduction to Focus Blocks](/FOCUS_BLOCKS.md) first to understand the motivation for the creation of this program.

**`fob`** is a command-line program that makes it easy to implement Focus Blocks in your daily life. It is written in Python and distributed as standalone binaries for Mac, Linux, and Windows.

# Quick Start

Download the program from the latest [Github release](https://github.com/tensorturtle/fob/releases) and put it somewhere on PATH.

`fob` is currently compiled and released for M-series Macs and Linux.

On Mac, you may need to go to "System Settings" -> "Privacy & Security" to allow `fob` to run. By default, Mac shows scary warnings and doesn't let you run just any program.

# Development

[Install uv](https://docs.astral.sh/uv/getting-started/installation/)

Clone this repository:
```
git clone https://github.com/tensorturtle/fob.git
cd fob
```

Run app in development:
```
uv run fob
```

The `--debug` option may be helpful. Also, the so-called database is actually just a human-readable/editable JSON file. Use `fob info` to see where the database is located.

# Test

```
uvx pytest
```

This is an end-to-end test. It installs `fob` to a temporary directory using `install.sh` and runs commands against it. Github Actions is set up to run the same test upon pushing to main branch.

# Release

From the root of this repository, run `./install.sh`. It uses pyinstaller to create a standalone binary and places it in `~/.local/bin` for access from anywhere on the system.

Create a new Github Release with a new tag and upload the executable. The binary is at: `dist/fob`.

# Features

## Share your database across different machines.

`fob` stores all state within a single database file (which is actually just a human-readable JSON file). Pass in a path on a shared drive (e.g. Dropbox) to the `--database` option when running `fob`. For example:

```
fob --database ~/Dropbox/my-fob.db help
```

For more convenience, you can export a `FOB_DB_PATH` variable in your shell.

For example, to use a database synchronized across devices on your Dropbox,
add the following line to `~/.bashrc` (for bash shell):
```
export FOB_DB_PATH="~/Dropbox/my-fob.db"
