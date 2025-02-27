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
