# Introduction

This project introduces the `hvtext` package which deals with text
processing. The package consists of:

* The fixed_width module which parses rows of text with fixed-width
  columns. The work horse in this package is the function `split_rows()`
  which, when given rows of text, will split them into fields.
* Key-value text parser

# Fixed-Width Columns Text

We often need to deal with fixed-width columns, for example, the
contents of the file *table.txt* is:

    USER              Alias   User ID  SHELL
    John Doe          johnd   501      bash
    Jane Doe          janed   502      tcsh
    Long John Silver  longjs  503      zsh

using `split_rows`, we can split these rows into fields, ready for
processing. See *parse_fixed_width_files.py*.

## Samples

* *parse_fixed_width_files.py*: Parse with and without guessing the
  columns
* *guess_does_not_work.py*: The package cannot guess right-justified
  columns

## Limitations

The function `guess_columns` does not work for the following cases:

* When one or more columns is right-justified
* When one or more cells are missing (empty)
* Tabs can cause confusion. At this point, tabs are just single
  characters
* If the number of rows are large, `guess_columns` still go through all
  of them, which might take a long time to finish. To minimize the
  impact, the caller can supply just a few rows (say 10) for guessing.

## Planned Improvements

* Add an optional parameter `limit=10` to limit the number of rows
  to guess
* Add tabs handling by introducing two new options
    1. Expand tabs (boolean)
    2. Tabs width (default=8)

# Key-Value Text Parser

We often deal with configuuration files such as:

    user: johnk
    auto-disconnect: true

or

    user = johnk
    auto-disconnect = true

Parsing these files are not hard, but it is a task that we performm
often, so it helps to create a reusable module to do it.

## Sample

The *kv_demo.py* file demonstrate the use of `textlib.kv.parse` to parse
several kinds of text.

## Limitations

* Not nested, for nested contents, please look into JSON or YAML


# Discard Text Lines

When processing text lines, we often need to discard certain lines
such as blank lines, or comments. The `discard` submodule provides this
functionality.

## Samples

* *csv_with_comment.py* demonstrates the use of `discard.blank()` and
  `discard.comment()` to parse a CSV file
* *parse_json_with_comments.py* demonstrates parsing JSON file with
  comments
