from argparse import Namespace

from fob.db.wrapper import TinyDBWrapper


def nvm(args: Namespace, db: TinyDBWrapper):
    '''
    'nvm' command: Abbreviation for 'Nevermind" - used to convert a non-Buffer block into a Buffer block.

    The user would run `fob sup` to see today's checklist.
    If they succeed in completing a block, they would run `fob did (number)` to mark the block as done.
    However, if they fail to do meaningful work on a block, or somehow circumstances made it so that they couldn't do the work assigned in that block, they can run `fob nvm (number)` to convert the block into a Buffer block and mark it as a complete Buffer block. Normally this kind of assignment is done one time at the beginning of the day through `fob gm`, but this command lets us override that.
    '''
    raise NotImplementedError("This command has not been implemented yet.")
