from argparse import Namespace

from fob.commands.init import default_db_path


def uninstall(args: Namespace) -> None:
    # Delete the database file and fob directory
    from os import remove, rmdir

    db_path = default_db_path()

    try:
        remove(db_path)
        rmdir(db_path.parent)
        print("\N{WHITE HEAVY CHECK MARK} Uninstalled fob.")
    except FileNotFoundError:
        print("\N{CROSS MARK} fob is not installed.")
        return
    except Exception as e:
        print("\N{CROSS MARK} An error occurred while uninstalling fob.")
        print(e)
        return
