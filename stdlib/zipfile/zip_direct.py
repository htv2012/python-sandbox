#!/usr/bin/env python3
# whatis: write/read directly to a zip file, must be in binary mode
import codecs
import zipfile


data = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
posuere massa sem, sed egestas tortor ultricies vitae. In nec ipsum
diam. Curabitur ipsum augue, tristique a sodales vel, venenatis at
ante. Suspendisse porttitor nibh quis ex consequat, sit amet viverra
turpis condimentum. Nullam vitae auctor tortor. Nulla dapibus,
mauris ut sodales efficitur, urna neque facilisis orci, eget accumsan
justo tellus ut neque. Maecenas turpis felis, mattis nec tortor et,
mattis sagittis purus. In non mauris nisi. Nam congue interdum
mollis. Suspendisse potenti. Maecenas lobortis ornare nunc ac dictum.
Nam aliquet eros sed efficitur commodo. Maecenas sodales velit ut
vehicula ullamcorper. Nullam venenatis facilisis iaculis. Curabitur
eget vulputate ligula, vitae pellentesque mi.
""".strip()

if __name__ == '__main__':
    with zipfile.ZipFile('data.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zip:
        with zip.open('data.txt', 'w') as outfile:
            outfile.write(codecs.encode(data))

    with zipfile.ZipFile('data.zip') as zip:
        with zip.open('data.txt') as infile:
            bytes = infile.read()
            message = codecs.decode(bytes)
            print(message)
