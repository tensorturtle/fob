
from fob.db.exc import DbIntegrityError

def write_new_month(working_days: int | None, blocks_per_day: int | None, blocks_per_area: dict[str, int] | None ):
    if working_days is None or blocks_per_day is None or blocks_per_area is None:
        raise DbIntegrityError("None or falsy values passed to write_new_month")
