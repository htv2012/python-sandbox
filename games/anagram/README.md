This directory deals with word anagrams, not phrase anagrams

# Scripts

- build.py: Creates anagrams.json
- find.py: Finds all the anagrams for a list of words
- list.py: Lists all the anagrams

The `build.py` script creates the data file `anagrams.json` which other scripts use.

# Examples

```bash
$ ./find.py nest mast angriest      # Find anagrams for these words
nest, nets, sent, tens
mast, mats, tams
angriest, gantries, ingrates, rangiest, tangiers, tasering

$ ./list.py                         # Lists all words which have anagrams

$ ./list.py -l 7                    # List words which has total of 7 anagrams, including themselves
ales, elsa, lase, leas, lesa, sale, seal
aster, rates, stare, tares, taser, tears, treas
carets, caster, caters, crates, reacts, recast, traces
least, slate, stael, stale, steal, tales, teals, tesla
pares, parse, pears, rapes, reaps, spare, spear
```
