from argparse import Namespace
from fob.db import TinyDBWrapper


def gm(args: Namespace, db: TinyDBWrapper) -> None:
    print(f"Good morning! {args}")
