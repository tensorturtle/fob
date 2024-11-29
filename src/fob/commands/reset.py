from argparse import Namespace
from os import remove, rmdir
from pathlib import Path

from rich import print
from rich.prompt import Prompt

from fob.utils import default_db_path

from fob.db import TinyDBWrapper


def reset(args: Namespace, db: TinyDBWrapper) -> None:
    db_path = args.database or default_db_path()
    if not isinstance(db_path, Path):
        db_path = Path(db_path)

    print(f"[red bold]Warning![/red bold] This will delete the database file at [cyan]{db_path}[/cyan].")

    if Prompt.ask("Are you sure?", choices=["yes", "no"], default="no") == "no":
        print("Reset cancelled.")
        return

    try:
        remove(db_path)
        print(f"\N{WHITE HEAVY CHECK MARK} [bold]Deleted[/bold] persistent database at [not bold][magenta]{db_path}[/not bold][/magenta].")
    except FileNotFoundError:
        pass
    try:
        if db_path.parent.name == 'fob':
            rmdir(db_path.parent)
            print(f"\N{WHITE HEAVY CHECK MARK} Also [bold]deleted[/bold] parent directory [cyan]'fob'[/cyan] at [not bold][magenta]{db_path.parent}[/not bold][/magenta].")
        else:
            print(f"[red]Warning:[/red] Parent directory [cyan]{db_path.parent}[/cyan] was not deleted. You may want to delete it manually.")
    except FileNotFoundError:
        pass

    print("\nNext: [green bold]fob new_month[/green bold]: Start a new month (creates a new database)")
