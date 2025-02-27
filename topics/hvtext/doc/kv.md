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


