from argparse import Namespace
from os import remove, rmdir

from rich import print
from rich.prompt import Prompt

from fob.utils import default_db_path

from fob.db import TinyDBWrapper


def reset(args: Namespace, db: TinyDBWrapper) -> None:
    print(f"[red bold]Warning![/red bold] This will delete the database at the default path.")
    if Prompt.ask("Are you sure?", choices=["yes", "no"], default="no") == "no":
        print("Reset cancelled.")
        return

    db_path = default_db_path()

    try:
        remove(db_path)
    except FileNotFoundError:
        pass
    try:
        rmdir(db_path.parent)
    except FileNotFoundError:
        pass
    print(f"\n\N{WHITE HEAVY CHECK MARK} [bold]Deleted[/bold] persistent database and directories at [not bold][magenta]{db_path}[/not bold][/magenta].")
    print("\nNext steps:")
    print("\t[green bold]fob new_month[/green bold]: Start a new month (creates a new database)")
