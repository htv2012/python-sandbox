import PIL.Image
import PIL.ImageChops
import PIL.ImageStat


# def root_mean_square(list1, list2):
#     sum_square = sum((a - b)**2 for a, b in izip(list1, list2))
#     print sum_square
#     return math.sqrt(sum_square / len(list1))


def calculate_diff_index(image1, image2):
    diff = PIL.ImageChops.difference(image1, image2)

    stat = PIL.ImageStat.Stat(image1)
    max_pixel_values = [max_value for min_value, max_value in stat.extrema]
    stat = PIL.ImageStat.Stat(diff)
    diff_indices = [1.0 * value / max_value for value, max_value in zip(stat.median, max_pixel_values)]
    diff_index = float(sum(diff_indices)) / len(diff_indices)
    return diff_index


def compare_images(file1, file2):
    image1 = PIL.Image.open(file1)
    image2 = PIL.Image.open(file2)
    diff_index = calculate_diff_index(image1, image2)
    print('{}\n{}\nDiff index = {:.3}'.format(file1, file2, diff_index))
    print('')

if __name__ == '__main__':
    compare_images('background.png', 'background2.jpg')
    compare_images('background.png', 'background3.jpg')
    compare_images('usa_map_640x480.gif', 'usa_map_copy_640x480.gif')
    compare_images('usa_map_640x480.gif', 'usa_map2_640x480.gif')
