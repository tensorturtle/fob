from argparse import Namespace

from fob.db import TinyDBWrapper
from fob.commands.components import month_overview, day_checklist

def sup(args: Namespace, db: TinyDBWrapper) -> None:
    month_overview(args, db)
    day_checklist(args, db)
