#!/usr/bin/env python

import ddt
import unittest

from atom.test_utilities.test_case_info import TestCaseInfo
from PIL import Image, ImageColor

def get_adjusted_histogram(image, washed_out_percentage):
    if image.mode not in {'RGB', 'RGBA'}:
        raise ValueError('Unsupported image mode: {}'.format(image.mode))

    # Get histogram, discard alpha channel
    image_histogram = image.histogram()[:768]
    band_boundary = [255, 511, 767]
    BAND_WIDTH = 256

    for color, count in enumerate(image_histogram):
        if count:
            boundary = band_boundary[color // BAND_WIDTH]
            washed_out = (boundary - color) * washed_out_percentage
            yield int(color + washed_out)


@ddt.ddt
class GetAdjustedHistogramTest(unittest.TestCase):
    longMessage = True
    data = [
        TestCaseInfo('none', wash=0.0, color='blue', expected=(0, 256, 767)),
        TestCaseInfo('30_percent', wash=0.3, color='red', expected=(255, 332, 588)),
        TestCaseInfo('40_percent', wash=0.4, color='green', expected=(102, 434, 614)),
        TestCaseInfo('50_percent', wash=0.5, color='purple', expected=(191, 383, 703)),
        TestCaseInfo('70_percent', wash=0.7, color='yellow', expected=(255, 511, 690)),
        TestCaseInfo('full', wash=1.0, color='blue', expected=(255, 511, 767)),
    ]

    @ddt.data(*data)
    def test_washed_out(self, test_case):
        image = Image.new(
            mode='RGBA', size=(1, 1),
            color=ImageColor.getcolor(test_case.color, 'RGBA'))
        actual = get_adjusted_histogram(image, test_case.wash)
        self.assertEqual(test_case.expected, tuple(actual))

    def test_multiple_color_points(self):
        image = Image.new(mode='RGB', size=(2, 2), color=(100, 100, 100))
        image.putpixel(xy=(0, 0), value=(200, 60, 40))
        actual = tuple(get_adjusted_histogram(image, 0.4))
        expected = (162, 222, 394, 418, 638, 674)
        self.assertEqual(expected, actual)

    @ddt.data('L', '1', 'P')
    def test_invalid_image(self, mode):
        image = Image.new(mode=mode, size=(1, 1))
        with self.assertRaises(ValueError):
            actual = tuple(get_adjusted_histogram(image, 0.7))


if __name__ == '__main__':
    unittest.main(verbosity=2)
