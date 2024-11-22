from rich import print
from argparse import Namespace

from fob.db import TinyDBWrapper

def help(args: Namespace | None, db: TinyDBWrapper | None) -> None:
    print("""
[green bold]Usage:[/green bold] [cyan][bold]fob[/bold] [OPTIONS] COMMAND[/cyan]

A personal month-level daily block scheduler.

[green bold]Common Commands:[/green bold]
    [cyan bold]help[/cyan bold]        Show this help information and quit
    [cyan bold]new_month[/cyan bold]   Allocate blocks for a new month
    [cyan bold]gm[/cyan bold]          Start a new day by selecting the blocks you will work on today.
    [cyan bold]sup[/cyan bold]         Quick look at the month and today's blocks
    [cyan bold]reset[/cyan bold]       Delete persistent database file.

[green bold]Global Options:[/green bold]
    [cyan bold]-d, --database[/cyan bold] [magenta not bold]<PATH_TO_DB_FILE>[/magenta not bold]  Path to database file. You can use a cloud storage (eg. Dropbox) to sync the database across devices.
    [cyan bold]-x, --debug[/cyan bold]  Enable debug mode.

First time with fob? Start by running [green][bold]fob new_month[/green][/bold] to allocate blocks for the month.""")
