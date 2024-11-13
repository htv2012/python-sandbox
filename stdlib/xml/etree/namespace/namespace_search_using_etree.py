#!/usr/bin/env python3
import xml.etree.ElementTree

text = """<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor>
        <name>John Cleese</name>
        <fictional:character>Lancelot</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor>
        <name>Eric Idle</name>
        <fictional:character>Sir Robin</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Commander Clement</fictional:character>
    </actor>
</actors>
"""

root = xml.etree.ElementTree.fromstring(text)
ns = {
    "default_ns": "http://people.example.com",
    "fictional": "http://characters.example.com",
}
for actor in root.findall("default_ns:actor", ns):
    name = actor.find("default_ns:name", ns)
    print(f"{name.text}")
    for character in actor.findall("fictional:character", ns):
        print(f"- {character.text}")
