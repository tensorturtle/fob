from argparse import Namespace

from fob.commands.init import default_db_path

def uninstall(args: Namespace) -> None:
    # Delete the database file and fob directory
    from os import remove, rmdir
    from pathlib import Path
    from platform import system

    db_path = default_db_path()

    try:
        remove(db_path)
        rmdir(db_path.parent)
        print(f"\N{white heavy check mark} Uninstalled fob.")
    except FileNotFoundError:
        print(f"\N{cross mark} fob is not installed.")
        return
    except Exception as e:
        print(f"\N{cross mark} An error occurred while uninstalling fob.")
        print(e)
        return
