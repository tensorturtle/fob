![banner](/assets/banner.png)

# `fob`
**A CLI program for implementing Focus Blocks in your daily life.**

[![Build & Test](https://github.com/tensorturtle/fob/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/tensorturtle/fob/actions/workflows/tests.yaml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Intro

![](/assets/fob-v0.2.6-sup-screenshot.png)

**Focus Blocks** is my take on time management inspired by Flow State, Pomodoro Technique, Timeboxing, and Deep Work. Please read the [Introduction to Focus Blocks](/FOCUS_BLOCKS.md) first to understand the motivation for the creation of this program.

**`fob`** is a simple CLI program that lets you plan your month, and then visualize & update your progress within the Focus Blocks time management framework.

It is written in Python with minimal dependencies and can be installed on Mac, Linux, and Windows.

# Quick Start

First, install `uv` (directions [here](https://docs.astral.sh/uv/getting-started/installation/))

Then, clone this repository to the directory of your choice.

```
git clone https://github.com/tensorturtle/fob.git
```

You can try out `fob` without installing it by using `uv run`:
```
uv run fob help
```

If you want to be able to call `fob` directly from your terminal, install it to your system:

```
./install.sh
```

This will compile and install `fob`. Now you can run:

```
fob help
```

# Features

## Cloud Sync

Bring your own cloud.

`fob` runs on a single database file. You can store this database on Dropbox or your own cloud. Just pass the path to the `--database` option when running `fob`. For example:

```
fob --database ~/Dropbox/my-fob.db help
```

For more convenience, you can export a `FOB_DB_PATH` variable in your shell.
For example, add the following line to `~/.bashrc` (for bash shell):
```
export FOB_DB_PATH="~/Dropbox/my-fob.db"
```

# Development

Run app in debug mode:
```
uv run fob --debug
```

Use database at custom path:
```
uv run fob --database ~/Downloads/testing_fob.db
```

The so-called database is actually just a human-readable JSON file. To see its location:
```
uv run fob info
```

# Testing

```
uvx pytest
```

This is an end-to-end test. It installs `fob` to a temporary directory using `install.sh` and runs commands against it. Github Actions is set up to run the same test upon pushing to main branch.

