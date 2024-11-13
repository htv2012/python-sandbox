#!/bin/sh
if [ -z "$1" ]
then
    echo "Run a script. For example"
    echo "-------------------------"
    for f in *.py
    do
        echo "$0 $f"
    done
else
    make SCRIPT="$1"
fi

