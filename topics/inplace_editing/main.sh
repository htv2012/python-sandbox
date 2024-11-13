#!/bin/bash

cp original.txt data.txt
python inplace.py data.txt

cat original.txt
echo '-----------'
cat data.txt