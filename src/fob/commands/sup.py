from argparse import Namespace

from fob.db import TinyDBWrapper
from fob.commands.overviews import month_overview
from fob.commands.user_flows import day_checklist

def sup(args: Namespace, db: TinyDBWrapper) -> None:
    month_overview(args, db)
    day_checklist(args, db)
