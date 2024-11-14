![banner](/assets/banner.png)

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# `fob`: Focus Blocks

## Quick Start

Download the program from the latest [Github release](https://github.com/tensorturtle/fob/releases) and put it somewhere on PATH.

A `curl | sh` type of installation script for the the lazy is coming soon.

`fob` runs on Mac, Linux, and Windows. In practice, it's only tested on Mac and Linux.

## Development

[Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)

Clone this repository:
```
git clone https://github.com/tensorturtle/fob.git
cd fob
```

Run app in development:
```
uv run fob
```

## Release

From the root of this repository, run `dev_install.sh`. It uses nuitka to compile the python code into a single file executable, and then installs it to the system.

# Inner Workings

## Database

[`TinyDB`](https://github.com/msiemens/tinydb) is used to persist the data as a human-readable JSON file.

Since we're not using a SQL database, we are responsible for upholding the integrity and consistency of the data before writing it to the database. We implement that by first receiving all the data from the user, validating it, and then 'commiting' (writing) to the database in one go.

Run the program with debug option `fob -x` or `fob --debug` to see how the database gets updated. Also, the so-called database is actually just a human-readable JSON file, so you can open that to inspect / edit it.
