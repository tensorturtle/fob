![banner](/assets/banner.png)

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# `fob`: Focus Blocks

## Getting Started

[Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)

Clone this repository:
```
git clone https://github.com/tensorturtle/fob.git
cd fob
```

Run app for the first time:
```
uv run fob init
```

# Inner Workings

## Database

[`TinyDB`](https://github.com/msiemens/tinydb) is used to persist the data as a human-readable JSON file.

Since we're not using a SQL database, we are responsible for upholding the integrity and consistency of the data before writing it to the database. We implement that by first receiving all the data from the user, validating it, and then 'commiting' (writing) to the database in one go.

Example schema:
```
{
  "year": 2024,
  "month": 12,
  "work_days_allocated": 20,
  "work_days_completed": 8,
  "blocks_per_day": 5,
  "areas": {
    "First Area": {
      allocated: 70,
      completed: 10,
    }
    "Second Area": {
      allocated: 30,
      completed: 30,
    }
  }
}
```
These constraints must be manually verified to be true within our database:
+ Total blocks (`work_days_allocated` * `blocks_per_day`) equals sum `allocated` field for each area.
+ `work_days_completed` equals sum of `completed` field for each area.
+ For each area, `completed` <= `allocated`
