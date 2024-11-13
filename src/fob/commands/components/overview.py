from argparse import Namespace
from datetime import date
from calendar import monthrange

from tinydb import where
from rich.pretty import pprint, Pretty
from rich.console import Console, Group
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TaskProgressColumn, TextColumn, ProgressColumn
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich import print
from rich.prompt import Prompt

from fob.db import TinyDBWrapper
from fob.db import checklist_complete

# Custom Column to display assigned / total values
class RawQuantityColumn(ProgressColumn):
    def render(self, task) -> Text:
        # Format as 'completed / total'
        completed_total = f"{task.completed:.0f} / {task.total:.0f}"
        return Text(completed_total, style="progress.data")

def display_checklist(args: Namespace, db: TinyDBWrapper) -> None:
    checklist = db.all()[0]['checklist']
    if args.debug:
        print("Checklist from DB:")
        pprint(checklist)
    # print the checklist
    for num, info in checklist.items():
        print(Panel(f"{num}: {info['name']}", border_style="bold green" if info['done'] else "bold red"))


def day_checklist(args: Namespace, db: TinyDBWrapper) -> None:
    try:

        checklist = db.all()[0]['checklist']
        if args.debug:
            print("Checklist from DB:")
            pprint(checklist)

        print("[bold]\nToday's Checklist:[/bold]")
        # create a new dict that creates an entry for each block

        display_checklist(args, db)

        if checklist_complete(db):
            print("\n[green]All blocks have been completed![/green]")
            print("Start a new day: [green bold]fob gm[/green bold]")
            return
        else:
            # get user input
            print("\n[bold]Mark blocks as completed:[/bold]")
            check_number = Prompt.ask(f"Which blocks have you completed? (1-{len(checklist)}): ")

            # mark the blocks as completed
            checklist[check_number].update({"done": True})

            if args.debug:
                print("Updated checklist:")
                pprint(checklist)

            # update db
            db.update({"checklist": checklist}, None)

            if args.debug:
                print("Updated database:")
                pprint(db.all())

            # updated checklist
            print("\n[green]Checklist updated![/green]\n")
            display_checklist(args, db)

            if checklist_complete(db):
                print("\n[green]All blocks have been completed![/green]")
                print("Start a new day: [green bold]fob gm[/green bold]")
                return

    except KeyError: # No 'today' entry
        print("[red][bold]No day data found.[/red][/bold]")


def month_overview(args: Namespace, db: TinyDBWrapper) -> None:
    today = date.today()
    data = db.search(where('year') == today.year and where('month') == today.month)[0]

    console = Console()

    m_progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        RawQuantityColumn(),
        disable=True
    )

    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        RawQuantityColumn(),
        disable=True # don't print immediately, print when called by console
    )

    today = date.today()
    days_in_month = monthrange(today.year, today.month)[1]

    with m_progress:
        task = m_progress.add_task(f"Month", total=days_in_month)
        m_progress.update(task, completed=today.day)

        task = m_progress.add_task(f"Work Days", total=data['work_days_allocated'])
        m_progress.update(task, completed=data['work_days_completed'])

    with progress:
        for area_name, blocks in data['areas'].items():
            task = progress.add_task(f"[bold]{area_name}[/bold]", total=blocks['allocated'])
            progress.update(task, completed=blocks['completed'])

    panel = Panel(Group(m_progress, Rule(style='cyan'), progress), title="This Month", border_style="bold cyan")
    console.print(panel)
