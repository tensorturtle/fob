# Creating a Single File Executable

`nuitka` is installed as a dev dependency.

To create a standalone executable:
```
uv run python -m nuitka --standalone src/fob/__init__.py --output-filename=fob
```

Run it:
```
cd __init__.dist
./fob
```

Copy it to somewhere on your PATH.
```
echo $PATH
```
On mac, recommended is: `/Users/$USER/.local/bin`:
```
cp __init__.dist/fob /Users/$USER/.local/bin
```

The `fob` executable is also uploaded to Github release page for each version release.

Clean up
```
rm -r __init__.dist __init__build
```
