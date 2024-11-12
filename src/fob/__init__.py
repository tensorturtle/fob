import sys
import argparse
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from rich import print

import fob.commands
from fob.utils import default_db_path, check_db_exists
from fob.db import TinyDBWrapper

def main():
    try:
        run_app()
    except KeyboardInterrupt:
        print("\n[red bold]Exiting.[/red bold]")
        sys.exit(1)

def run_app():
    if len(sys.argv) == 1:
        print(
            '''[red][bold]Incorrect usage.[/bold][/red]

[green][bold]Usage:[/bold][/green] [cyan][bold]fob[/bold] [OPTIONS] <command>[/cyan]

Try [cyan bold]fob help[/cyan bold] for usage information.
'''
        )
        sys.exit(1)

    # use our custom help page `fob help` instead of default argparse (`-h` or `--help`)
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        fob.commands.help(None, None)
        sys.exit(0)

    parser = argparse.ArgumentParser(
        prog="fob",
        description="A personal month-level daily block scheduler.",
        add_help=False,  # because we're using our own help page'
    )
    parser.add_argument(
        "-d", "--database", type=str, help="Optional custom path to database file."
    )
    subparsers = parser.add_subparsers(dest="command", help="Common Commands")
    subparsers.add_parser("help", help="Show help information and quit")
    subparsers.add_parser("new_month", help="Allocate blocks for a new month")
    subparsers.add_parser(
        "gm", help="Start a new day by selecting the blocks you will work on today"
    )
    subparsers.add_parser("gn", help="Say good night")
    subparsers.add_parser("reset", help="Reset fob by deleting persistent database file.")

    args = parser.parse_args()

    command_func = None
    try:
        command_func = getattr(fob.commands, args.command)
    except AttributeError:
        print(
            f"[red bold]fob {args.command}[/red bold] is not a valid fob command.\nSee [green bold]fob help[/green bold] for usage information."
        )
        sys.exit(1)

    if not args.database:
        # create necessary directories for default path in case they don't exist
        default_db_path().parent.mkdir(parents=True, exist_ok=True)

    db_path = Path(args.database or default_db_path())
    if check_db_exists(args):
        print(f"Using [bold]existing[/bold] database at [not bold][magenta]{db_path}[/not bold][/magenta]")
    else:
        print(
            f"\N{WHITE HEAVY CHECK MARK} [bold]Created[/bold] new database at [not bold][magenta]{db_path}[/not bold][/magenta]"
        )
    db = TinyDBWrapper(db_path)

    command_func(args, db)
