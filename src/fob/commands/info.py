from argparse import Namespace
import importlib.metadata

from rich.pretty import pprint
from rich import print

from fob.db.wrapper import TinyDBWrapper


def info(args: Namespace, db: TinyDBWrapper):
    '''
    'info' command displays basic metadata about this program.

    + Version
    + Author
    + License
    '''
    return
