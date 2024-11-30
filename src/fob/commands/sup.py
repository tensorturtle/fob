from argparse import Namespace

from rich import print

from fob.db import TinyDBWrapper
from fob.commands.overviews import month_overview, display_checklist

def sup(args: Namespace, db: TinyDBWrapper) -> None:
    '''
    A quick look at the month and today's blocks. No user input required and no modifications to the database.
    '''
    month_overview(args, db)
    display_checklist(args, db)
    print("Next commands: [green][bold]fob did (number)[/green][/bold] check off today's blocks.")
