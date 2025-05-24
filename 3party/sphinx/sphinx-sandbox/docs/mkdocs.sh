#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# shellcheck source=/dev/null
source "$SCRIPT_DIR/../.venv/bin/activate"

# Prep the build dir
cd "$SCRIPT_DIR" || exit
rm -fr build
mkdir build
cp -R source build

# Build
sphinx-apidoc -o build/source ../src
sphinx-build build/source build
xdg-open build/index.html

