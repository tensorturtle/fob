from argparse import Namespace
from rich.pretty import pprint
from rich.panel import Panel
from rich import print
from rich.prompt import Prompt

from fob.db import TinyDBWrapper
from fob.db import checklist_complete

def display_checklist(args: Namespace, db: TinyDBWrapper) -> None:
    try:
        checklist = db.all()[0]['checklist']
    except KeyError:
        print("[red][bold]No day data found.[/red][/bold]")
        print("Run [cyan][bold]fob gm[/cyan][/bold] to start a new day.")
        return
    if args.debug:
        print("Checklist from DB:")
        pprint(checklist)
    # print the checklist
    for num, info in checklist.items():
        print(Panel(f"{num}: {info['name']}", border_style="bold green" if info['done'] else "bold red"))

def day_checklist(args: Namespace, db: TinyDBWrapper) -> None:
    try:
        try:
            checklist = db.all()[0]['checklist']
        except IndexError:
            print("[red][bold]No day data found.[/red][/bold]")
            print("Run [cyan][bold]fob gm[/cyan][/bold] to start a new day.")
            return
        if args.debug:
            print("Checklist from DB:")
            pprint(checklist)

        print("[bold]\nToday's Checklist:[/bold]")
        display_checklist(args, db)

        if checklist_complete(db):
            print("\n[green]All blocks have been completed![/green]")
            print("Start a new day: [green bold]fob gm[/green bold]")
            return
        else:
            print("\n[bold]Mark blocks as completed:[/bold]")
            check_number = Prompt.ask(f"Which blocks have you completed? (1-{len(checklist)}): ")

            try:
                checklist[check_number].update({"done": True})
            except KeyError:
                print("[red][bold]Invalid block number.[/red][/bold]")
                return

            if args.debug:
                print("Updated checklist:")
                pprint(checklist)

            db.update({"checklist": checklist}, None)

            if args.debug:
                print("Updated database:")
                pprint(db.all())

            print("\n[green]Checklist updated![/green]\n")
            display_checklist(args, db)

            if checklist_complete(db):
                print("\n[green]All blocks have been completed![/green]")
                print("Start a new day: [green bold]fob gm[/green bold]")
                return

    except KeyError as e:  # No 'today' entry
        print("[red][bold]No day data found.[/red][/bold]")
        if args.debug:
            print(f"KeyError: {e}")
