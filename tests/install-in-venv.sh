#!/bin/sh

if ! [ -e "$1" ]; then
  echo "Usage: ./scripts/install-in-venv.sh ../../path/to/my/.venv/bin/activate" >&2
  exit 1
fi

. $1
poetry build --format sdist

if [[ "$OSTYPE" == "darwin"* ]]; then
    tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py
else
    tar -xvf dist/*-`poetry version -s`.tar.gz -O --wildcards '*/setup.py' > setup.py
fi

python setup.py develop
deactivate
