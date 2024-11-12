from argparse import Namespace

from rich import print

from fob.utils import default_db_path

from fob.db import TinyDBWrapper


def reset(args: Namespace, db: TinyDBWrapper) -> None:
    # Delete the database file and fob directory
    from os import remove, rmdir

    db_path = default_db_path()

    try:
        remove(db_path)
    except FileNotFoundError:
        pass
    try:
        rmdir(db_path.parent)
    except FileNotFoundError:
        pass

    print(f"\N{WHITE HEAVY CHECK MARK} [bold]Deleted[/bold] persistent database and directories at [not bold][magenta]{db_path}[/not bold][/magenta].")
    print("Next steps:")
    print("\t[green bold]fob new_month[/green bold]: Start a new month (creates a new database)")
