from argparse import Namespace
from fob.db import TinyDBWrapper

def gn(args: Namespace, db: TinyDBWrapper) -> None:
    print("Good night! \N{GRINNING FACE}")
