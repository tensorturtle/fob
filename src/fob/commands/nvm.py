from argparse import Namespace
from datetime import date

from tinydb import where, Query
from rich.pretty import pprint
from rich import print
from rich.prompt import Prompt

from fob.commands.overviews.day_checklist import display_checklist
from fob.db.wrapper import TinyDBWrapper


def nvm(args: Namespace, db: TinyDBWrapper):
    '''
    'nvm' command: Abbreviation for 'Nevermind" - used to convert a non-Buffer block into a Buffer block.

    The user would run `fob sup` to see today's checklist.
    If they succeed in completing a block, they would run `fob did (number)` to mark the block as done.
    However, if they fail to do meaningful work on a block, or somehow circumstances made it so that they couldn't do the work assigned in that block, they can run `fob nvm (number)` to convert the block into a Buffer block and mark it as a complete Buffer block. Normally this kind of assignment is done one time at the beginning of the day through `fob gm`, but this command lets us override that.
    This command fails and doesn't do anything in case there are no Buffer blocks left this month.
    '''
    today = date.today()
    try:
        data = db.search(where('year') == today.year and where('month') == today.month)[0]
    except IndexError:
        print("[red][bold]No month data found.[/red][/bold]")
        print("Run [cyan][bold]fob new_month[/cyan][/bold] to start a new month.")
        return

    if args.debug:
        pprint(data)

    try:
        buffer_entry = data['areas']['Buffer']
    except KeyError:
        print("[red][bold]Program Error: Database seems to be malformed.[/red][/bold] (Database value at ['areas']['Buffer'] doesn't exist. Please report this issue. In the meantime, consider [cyan]fob reset[/cyan] to delete the database and start fresh.")
        return

    if args.debug:
        print("Buffer entry:")
        pprint(buffer_entry)

    buffer_blocks_left = buffer_entry['allocated'] - buffer_entry['completed']

    if buffer_blocks_left <= 0:
        print("[red][bold]No Buffer blocks left this month.[/red][/bold], so you can't convert any more blocks to Buffer blocks.")
        print("Consider running: [cyan][bold]fob new_month[/cyan][/bold] if you want to reset the block allocations for this month.")
        return

    # show user today's checklist
    # also is a guard for: there are blocks assigned to this day (it could be that right before the first day of the month, the checklist is empty.)
    display_checklist(args, db)

    # ask user which number they want to convert to buffer block
    try:
        num_to_convert = int(Prompt.ask("Which number would you like to convert to a Buffer block?", default="1"))
        # validate input to be between 1 and number of blocks today
        num_blocks_today = len(data['checklist'])
        if num_to_convert < 1 or num_to_convert > num_blocks_today:
            print("[red][bold]Please enter a number that corresponds to the checklist item[/red][/bold]")

        # fetch area name for that number
        # convert index back to string because keys in db are string
        area_to_decrement = data['checklist'][str(num_to_convert)]['name']

        if area_to_decrement == 'Buffer':
            print("[red][bold]Error: This block is already a Buffer block.[/red][/bold]")
            return

        if args.debug:
            print("Field to decrement:")
            print(area_to_decrement)

        # first, modify checklist
        data['checklist'][str(num_to_convert)]['name'] = "Buffer"
        data['checklist'][str(num_to_convert)]['done'] = True

        # second, modify area assignments
        data['areas']['Buffer']['completed'] += 1
        data['areas'][area_to_decrement]['completed'] -= 1

    except ValueError:
        print("[red][bold]Please enter a number that corresponds to the checklist item[/red][/bold]")
    except KeyError:
        print("[red][bold]Program Error: Database seems to be malformed.[/red][/bold] Please report this issue. In the meantime, consider [cyan]fob reset[/cyan] to delete the database and start fresh.")
        return

    q = Query()
    db.update({"areas": data['areas']}, q.year == today.year and q.month == today.month)
    db.update({"checklist": data['checklist']}, None)

    # print success message
    display_checklist(args, db)
    print(f"[green][bold]Block {num_to_convert} converted to Buffer block successfully.[/green][/bold]")
