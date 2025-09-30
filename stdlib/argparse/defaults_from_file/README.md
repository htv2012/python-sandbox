# Demo: Get defaults from files

When using argparse, we usually specify the defaults in the
script. However, there are times when we want to store the defaults in
one or more files. This project demonstrates that idea.

There are two defaults file. The first is `defaults.json`, which store
the original defaults. This file is created manually.

The second is `last.json`, which stores the defaults of the last run. It
will take precedence over `defaults.json`. This file is created by
the script.
