from argparse import Namespace

from fob.db.wrapper import TinyDBWrapper


def info(args: Namespace, db: TinyDBWrapper):
    '''
    'info' command displays basic metadata about this program.

    + Version
    + Author
    + License
    '''
    return
