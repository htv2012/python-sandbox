#!/usr/bin/env python3
import qrcode

img = qrcode.make("https://pillow.readthedocs.io")
img.save("save.png")
