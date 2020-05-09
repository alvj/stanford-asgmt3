"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    
    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(get_random(), get_random(), get_random())
            append_patch(patch, final_image, row, col)

    final_image.show()

def get_random():
    return random.randint(0, 20) / 10

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def append_patch(patch, image, row, col):
    for x in range(patch.width):
        for y in range(patch.height):
            pixel = patch.get_pixel(x, y)
            image.set_pixel(x + (PATCH_SIZE * col), y + (PATCH_SIZE * row), pixel)

if __name__ == '__main__':
    main()