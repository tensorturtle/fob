![banner](/assets/banner.png)


# `fob`
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**Focus Blocks** is my take on time management inspired by Flow State, Pomodoro Technique, Timeboxing, and Deep Work.

**`fob`** is a command-line program written in Python that is made from scratch to help you use Focus Blocks in your daily life. It is distributed as a standalone binary that runs on Mac, Linux, and Windows.

## Introduction

### How to use Focus Blocks

1. At the start of the month, decide the total number of blocks and the number of blocks you want to allocate to each area.
2. Each morning, choose to work on areas that have blocks remaining.
3. Throughout the day, check off blocks as you finish working on them.
4. At night, review. If necessary, modify the day's allocation of blocks to reflect what actually ended up happening.

### Important Concepts

+ **Block**: A period of focused work. (1.5 to 3 hours recommended). 
+ **Buffer**: When assigning blocks at the beginning of the month, it is highly recommended to reserve Buffer blocks. Buffer blocks are meant to be used when, due to unforeseen circumstances, you failed to spend a given block as allocated.

### Tips for using Focus Blocks in your life

Focus Blocks works best in conjunction with a longer-term and a shorter-term planning system.
+ Longer-term: Your monthly block allocation should be informed by a year or multi-year vision / goal.
+ Shorter-term: Focus Blocks only define what task you will do during the focused work hours of your day. You should have a daily routine that wraps Focus Blocks with a morning routine, break activities, and evening routine.

Focus Blocks makes the assumption that a given day is classified either as "Work Day" or "Play Day". This reflect my opinion that on rest days, you should really rest, and work days should be strictly structured the whole day. Therefore the total number of blocks in a month is simply `blocks_per_day` * `working_days_per_month`.

**The full story:** In the past (2020-2023), I have used Google Sheets to implement this functionality but it didn't offer the interactivity, simplicity, beauty, and customizability that I desired. Plus, writing Python for fun is fun. `fob` the CLI program was released on November 14, 2024.

### Benefits / Magic of Focus Blocks

+ Compared to regular to-do lists or Kanban boards, Focus Blocks gives you a more regular sense of achievement, because you can still check off a block as complete as long as you did you best, instead of accomplishing a given task (nevermind how tasks aren't really complete)
+ Focus Blocks makes the "illusion of free will" work **for** you, not against you. Typically, you will enjoy working on some areas more than others. With a less flexible system, you will feel pressured and negative about having to work the less enjoyable thing and probably will put it off. Focus Blocks gives you agency in 'choosing' to work on the less enjoyable thing, because you have to get it done anyhow. Plus, by decoupling blocks from to-do lists, you will feel less pressure on tasks that justifiably take more than a couple hours to achieve visible results.

## Quick Start

Download the program from the latest [Github release](https://github.com/tensorturtle/fob/releases) and put it somewhere on PATH.

A `curl | sh` type of installation script for the the lazy is coming soon.

`fob` runs on Mac, Linux, and Windows. In practice, it's only tested on Mac and Linux.

On Mac, you may need to go to "System Settings" -> "Privacy & Security" to allow `fob` to run. By default, Mac shows scary warnings and doesn't let you run just any program.

## Development

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

## Release

From the root of this repository, run `dev_install.sh`. It uses nuitka to compile the python code into a single file executable, and then installs it to the system.

# Inner Workings

## Database

[`TinyDB`](https://github.com/msiemens/tinydb) is used to persist the data as a human-readable JSON file.

Since we're not using a SQL database, we are responsible for upholding the integrity and consistency of the data before writing it to the database. We implement that by first receiving all the data from the user, validating it, and then 'commiting' (writing) to the database in one go.

Run the program with debug option `fob -x` or `fob --debug` to see how the database gets updated. Also, the so-called database is actually just a human-readable JSON file, so you can open that to inspect / edit it.
