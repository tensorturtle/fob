![banner](/assets/banner.png)

# `fob`
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**Focus Blocks** is my take on time management inspired by Flow State, Pomodoro Technique, Timeboxing, and Deep Work. Please read the [Introduction to Focus Blocks](/FOCUS_BLOCKS.md) first to understand the motivation for the creation of this program.

**`fob`** is a command-line program that makes it easy to implement Focus Blocks in your daily life. It is written in Python and distributed as standalone binaries for Mac, Linux, and Windows.

# Quick Start

Download the program from the latest [Github release](https://github.com/tensorturtle/fob/releases) and put it somewhere on PATH.

A `curl | sh` type of installation script for the the lazy is coming soon™.

`fob` is currently compiled and released for ARM Mac (M1 onwards) just because that's the machine I run it on. Testing and support for Windows and Ubuntu is coming soon™.

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

# Release

From the root of this repository, run `dev_install.sh`. It uses nuitka to compile the python code into a single file executable, and then installs it to the system.

Create a new Github Release with a new tag and upload the executable (path should be shown by `dev_install.sh`) to the Github Release.

# Features

## Share your database across different machines.

`fob` stores all state within a single database file (which is actually just a human-readable JSON file). Pass in a path on a shared drive (e.g. Dropbox) to the `--database` option when running `fob`. For example:

```
fob --database ~/Dropbox/my-fob.db help
```

For more convenience, you can export a `FOB_DB_PATH` variable in your shell.
For example, if you're using bash shell, add the following line to `~/.bashrc`:
```
export FOB_DB_PATH="~/Dropbox/my-fob.db"
```

# Inner Workings

## Database

[`TinyDB`](https://github.com/msiemens/tinydb) is used to persist the data as a human-readable JSON file.

Since we're not using a SQL database, we are responsible for upholding the integrity and consistency of the data before writing it to the database. We implement that by first receiving all the data from the user, validating it, and then 'commiting' (writing) to the database in one go.

Run the program with debug option `fob -x` or `fob --debug` to see how the database gets updated. Also, the so-called database is actually just a human-readable JSON file, so you can open that to inspect / edit it if you're developing `fob`. Use `fob info` to see where the database is located.

## Compiling to C

We use [`nuitka`](https://nuitka.net/) to compile to C in order to create self-contained binaries for each platform. See [`dev_install.sh`](/dev_install.sh) for how  it's used.
