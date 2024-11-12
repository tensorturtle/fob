import os
from pathlib import Path
import platform
import importlib.metadata

def get_app_version() -> tuple[str, str, str]:
    '''
    Reads the version (expected to be semver or similar (with three items separated by two dots))
    from pyproject.toml and returns it as a tuple of three strings.
    Not converted to ints because semver allows for non-numeric values.
    '''
    version_string_of_foo = importlib.metadata.version('fob')
    major, minor, revision = version_string_of_foo.split(".")
    return (major, minor, revision)

def default_db_path() -> Path:
    match platform.system():
        case "Windows":
            base_path = Path(os.getenv("APPDATA") or os.getenv("LOCALAPPDATA") or "")
        case "Darwin":
            base_path = Path.home() / "Library" / "Application Support"
        case "Linux":
            base_path = Path(
                os.getenv("XDG_DATA_HOME", Path.home() / ".local" / "share")
            )
        case _:
            raise OSError(f"Unsupported platform: {platform.system()}")

    # we couple the database file name with the semver to force a new database on minor version changes
    # this is a simple way to ensure that the schema is up to date
    # on the user side, they should plan to update the app at the same time as when they are planning for the next month.
    app_version = get_app_version()
    major_and_minor_version = f"{app_version[0]}.{app_version[1]}"
    database_path = base_path / "fob" / f"app-{major_and_minor_version}.db"
    return database_path

def check_db_exists(args) -> bool:
    database_path = Path(args.database or default_db_path())
    return database_path.exists()
