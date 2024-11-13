#!/bin/bash

cp original.txt data.txt
python first_line.py data.txt

cat original.txt
echo '-----------'
cat data.txt