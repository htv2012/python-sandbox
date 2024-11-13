#!/usr/bin/env python3
import argparse
import pathlib

from PIL import Image


def add_logo(image_path, logo_path, output_path):
    print(f"{image_path} + {logo_path} => {output_path}")
    image = Image.open(image_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    # Scale the logo to 1/10 of the image (use the longer dimension)
    scale = max(image.size) / 10.0 / max(logo.size)
    print(f"Size: {image.size}, Scale: {scale}")
    new_logo_size = tuple(int(d * scale) for d in logo.size)
    print(f"Logo size before: {logo.size}, After: {new_logo_size}")
    logo = logo.resize(new_logo_size)

    # Calculate the origin for the logo
    origin = max(image.size) // 10

    image = image.convert("RGB")
    image.paste(logo, (origin, origin), logo)
    image.save(output_path)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--logo", type=pathlib.Path, required=True)
    parser.add_argument("-i", "--input-dir", type=pathlib.Path, required=True)
    parser.add_argument("-o", "--output-dir", type=pathlib.Path, required=True)
    options = parser.parse_args()
    print("Options:", options)
    return options

def main():
    options = parse_command_line_arguments()
    options.output_dir.mkdir(exist_ok=True)
    #logo_path = options.input_dir / "wfh3.png"

    for image_path in options.input_dir.glob("*.jpg"):
        output_path = options.output_dir / image_path.name
        add_logo(image_path, options.logo, output_path)



if __name__ == '__main__':
    main()
