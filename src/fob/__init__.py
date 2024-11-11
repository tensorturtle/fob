import sys

from rich import print

import fob.commands

def main() -> None:
    if not sys.argv[1:]:
        commands.help(sys.argv[2:])
    else:
        try:
            getattr(commands, sys.argv[1])(sys.argv[2:])
        except AttributeError as e:
            print(f"[red bold]fob {sys.argv[1]}[/red bold] is not a valid fob command.\nSee [green bold]fob help[/green bold] for usage information.")
