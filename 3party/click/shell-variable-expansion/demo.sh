#!/usr/bin/env bash

echo ""
echo "\nDouble Quote"
uv run main.py "ls $HOME; ~ is where the heart is; echo $USER"

echo ""
echo "\nSingle Quote"
uv run main.py 'ls $HOME; ~ is where the heart is; echo $USER'
