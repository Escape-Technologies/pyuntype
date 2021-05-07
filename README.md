# Python untype

Programatically untype your Python Projects.

## Credits

The original idea and code of this project comes from the following [Stack OverFlow thread](https://stackoverflow.com/questions/42733877/remove-type-hints-in-python-source-programmatically).

## Install

```bash
pip install pyuntype
```

## Usage

Use the following command to completely untype your Python Project located in the `src/` folder.

```bash
pyuntype src/ dest/
```

### Option `gitmode` (bool)

When `--gitmode=True`, the `src` directory should be a inside a Git repository. The goal to create a `dest` folder only with the files listed by `git ls-files` (and thus taking into account `.gitignore`)

### Option `custom_typing_module` (str)

If you defined in your code a file with custom types, all imports from this file will be ignored, and this file won't be copied in your `dest` directory

### Example:

For the Python CLI, we can use:

```
pyuntype python python_untype --gitmode=True --custom_typing_module=custom_types
```

## Contribute

### Development install

Feel free to contribute by proposing merge requests to this project.

This project uses [Poetry](https://python-poetry.org/docs/basic-usage/) and can be installed in development mode with the following steps:

- `git clone https://github.com/Escape-Technologies/pyuntype.git && cd pyuntype`
- `poetry shell`
- `poetry install`

### Pre-commit

This project [Pre-Commit](https://pre-commit.com) to lint your code and make sure it is compliant to the rules we fixed.

```bash
pre-commit install --hook-type commit-msg
```

### Testing --wip--

This project uses [PyTest](https://docs.pytest.org/en/6.2.x/) to unit test the code.
