import sys
import argparse
from pathlib import Path

from rich import print

import fob.commands

def main():
    if len(sys.argv) == 1:
        print("No command provided. See [green bold]fob help[/green bold] for usage information.")
        sys.exit(1)

    # use our custom help page `fob help` instead of default argparse (`-h` or `--help`)
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        fob.commands.help(None)
        sys.exit(0)

    parser = argparse.ArgumentParser(
        prog='fob',
        description='A personal month-level daily block scheduler.',
        add_help=False # because we're using our own help page'
    )
    parser.add_argument(
        '-d', '--database',
        type=str,
        help='Optional custom path to database file.'
    )
    subparsers = parser.add_subparsers(dest='command', help='Common Commands')
    subparsers.add_parser('init', help='Create new database')
    subparsers.add_parser('help', help='Show help information and quit')
    subparsers.add_parser('new_month', help='Allocate blocks for a new month')
    subparsers.add_parser('gm', help='Start a new day by selecting the blocks you will work on today')
    subparsers.add_parser('gn', help='Say good night')

    args = parser.parse_args()

    if args.database:
        print(f"[bold]Using database:[/bold] {args.database}")

    command_func = None
    try:
        command_func = getattr(fob.commands, args.command)
    except AttributeError as e:
        print(f"[red bold]fob {args.command}[/red bold] is not a valid fob command.\nSee [green bold]fob help[/green bold] for usage information.")
        sys.exit(1)

    command_func(args)

if __name__ == "__main__":
    main()
