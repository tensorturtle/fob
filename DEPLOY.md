# Creating a Single File Executable

`nuitka` is installed as a dev dependency.

To create a standalone executable:
```
uv run python -m nuitka --standalone --onefile src/fob/__init__.py --output-filename=fob
```

Try running the resulting binary:
```
./fob
```

Copy it to somewhere on your PATH.
```
echo $PATH
```
On mac, recommended is: `/Users/$USER/.local/bin`:
```
mkdir -p /Users/$USER/.local/bin
cp fob /Users/$USER/.local/bin
```

Now, it can be run from anywhere on your system:
```
fob
```

The `fob` executable is also uploaded to Github release page for each version release.

Clean up
```
rm -r __init__.dist __init__build
```
