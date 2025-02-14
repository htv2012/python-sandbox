#!/usr/bin/env bash

echo hello

export hostname=foo.com
export port=22
export username=user1; export password=i4GOT
export myhome="/home/$username"

# BUG: The following failed to parse
export myhome2=/home/$username

source "vars.sh"

echo end

