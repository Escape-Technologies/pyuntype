"""Remove Python 3 hints."""

import os
import ast
import subprocess
from shutil import copyfile

import click
import astor
from loguru import logger

from pyuntype_cli import __version__
from pyuntype_cli.utils.title import title
from pyuntype_cli.utils.remover import TypeHintRemover


def remove_type_hints(source: str, custom_typing_module: str):
    """ Remove type hints from the source file"""

    # parse the source code into an AST
    parsed_source = ast.parse(source, feature_version=(3, 9))
    # remove all type annotations, function return type definitions
    # and import statements from 'typing'
    transformed = TypeHintRemover(custom_typing_module=custom_typing_module).visit(parsed_source)
    # convert the AST back to source code
    return astor.to_source(transformed)


@click.command()
@click.argument('src', type=str, required=True)
@click.argument('dest', type=str, required=True)
@click.option('--gitmode', type=bool, required=False)
@click.option('--custom_typing_module', type=str, default=None, required=False)
@logger.catch
def main(src: str, dest: str, gitmode: str, custom_typing_module: str) -> None:
    """Starting point of the Python CLI."""

    title()

    if gitmode:
        os.chdir(src)
        filenames = subprocess.check_output("git ls-files", shell=True).splitlines()
        filenames = [file.decode("utf-8") for file in filenames]
        os.chdir('..')
    else:
        filenames = [os.path.join(subdir, file) for subdir, _, files in os.walk(src) for file in files]

    for file in filenames:

        src_filepath = os.path.join(src, file)
        dest_filepath = os.path.join(dest, file)
        os.makedirs(os.path.dirname(dest_filepath), exist_ok=True)

        if src_filepath.endswith('.py'):

            if custom_typing_module:
                if custom_typing_module in file:
                    continue

            with open(src_filepath, 'r') as src_file:
                src_content = '\n'.join(src_file.readlines())

            dest_content = remove_type_hints(src_content, custom_typing_module)

            with open(dest_filepath, 'w') as dest_file:
                dest_file.write(dest_content)

        else:
            copyfile(src_filepath, dest_filepath)
