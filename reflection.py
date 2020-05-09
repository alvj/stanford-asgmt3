"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    # Create a new blank image with the same width but double the height
    reflected = SimpleImage.blank(image.width, image.height * 2)

    # Loop through every coordinate in the image
    for x in range(image.width):
        for y in range(image.height):
            # Get the pixel for each x and y coords
            pixel = image.get_pixel(x, y)
            # Set that pixel in the same position in the new image and also set it in the reflected position
            reflected.set_pixel(x, y, pixel)
            reflected.set_pixel(x, reflected.height - y - 1, pixel)

    return reflected


def main():
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
