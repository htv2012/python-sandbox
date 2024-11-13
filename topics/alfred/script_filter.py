#!/usr/bin/env python3
import typing

# {"items": [
#     {
#         "uid": "desktop",
#         "type": "file",
#         "title": "Desktop",
#         "subtitle": "~/Desktop",
#         "arg": "~/Desktop",
#         "autocomplete": "Desktop",
#         "icon": {
#             "type": "fileicon",
#             "path": "~/Desktop"
#         }
#     }
# ]}


class ScriptFilterItem(typing.TypedDict, total=False):
    uid: str
    type: str
    title: str
    subtitle: str
    arg: str
    autocomplete: str
    valid: bool
    match: str    
