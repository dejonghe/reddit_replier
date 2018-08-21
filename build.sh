#!/bin/bash

pandoc -f markdown  README.md -t rst -o README.rst
python setup.py sdist
