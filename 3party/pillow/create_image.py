#!/usr/bin/env python

from atom.test_utilities import image_processing
import argparse


def get_options():
    allowed_modes = '1 L P RGB RGBA CMYK YCbCr LAB HSV I F'.split()
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-b', '--bgcolor', default='white')
    parser.add_argument('-m', '--mode', default='RGB', choices=allowed_modes)
    parser.add_argument('-s', '--size', nargs=2, type=int, default=(640, 480))
    parser.add_argument('-a', '--alpha', type=int, default=255)
    options = parser.parse_args()
    return options


def main():
    options = get_options()
    print(options)

    image_processing.create_reference_image(
        options.output, options.mode, options.size, options.bgcolor, options.alpha)


if __name__ == '__main__':
    main()
