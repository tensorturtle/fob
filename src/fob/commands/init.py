import os
import sqlite3
from pathlib import Path
import platform
from argparse import Namespace

from rich import print

def init(args: Namespace) -> None:
    if not args.database:
        default_db_path().parent.mkdir(parents=True, exist_ok=True)
    database_path = Path(args.database or default_db_path())
    if not database_path.exists():
        apply_schema(database_path)
        print(f"\N{white heavy check mark} Created new database at [magenta]{database_path}[/magenta]")
        print(f"\N{white heavy check mark} Applied database schema.")

def apply_schema(db_path: Path) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE month (id INTEGER PRIMARY KEY, year INTEGER, month INTEGER, total_blocks INTEGER)")

    con.commit()
    con.close()

def default_db_path() -> Path:
    match platform.system():
        case "Windows":
            base_path = Path(os.getenv('APPDATA') or os.getenv('LOCALAPPDATA') or "")
        case "Darwin":
            base_path = Path.home() / 'Library' / 'Application Support'
        case "Linux":
            base_path = Path(os.getenv('XDG_DATA_HOME', Path.home() / '.local' / 'share'))
        case _:
            raise OSError(f"Unsupported platform: {platform.system()}")
    database_path = base_path / "fob" / "app.db"
    return database_path
