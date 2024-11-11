from rich import print

def help(command_args: list[str]) -> None:
    print('''
[green bold]Usage:[/green bold] [cyan bold]fob[/cyan bold] [OPTIONS] COMMAND

A personal month-level daily block scheduler.

[green bold]Common Commands:[/green bold]
    [cyan bold]init[/cyan bold]        Create new database.
    [cyan bold]help[/cyan bold]        Show this help information and quit
    [cyan bold]new_month[/cyan bold]   Allocate blocks for a new month
    [cyan bold]gm[/cyan bold]          Start a new day by selecting the blocks you will work on today.
    [cyan bold]
    [cyan bold]gn[/cyan bold]          Say good night

[green bold]Global Options:[/green bold]
    [cyan bold]-d, --database[/cyan bold] [magenta not bold]<PATH_TO_DB_FILE>[/magenta not bold]  Path to database file.
''')
