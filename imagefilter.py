# run pip install pillow to install
from PIL import Image
import math

def main():
    # Open image
    image = Image.open('nightbee.png')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    gray_ask = input("Choose between grayscale function 1 or 2 (type 1 or 2): ")
    if gray_ask == "1":
        # iterates through all pixels vertical for every horizontal pixel that is being iterated through
        for x in range(width):
            for y in range(height):
                # gets the rgb values for evry single pixel after the iteration is done
                r, g, b = image.getpixel((x, y))
                gray = int((r + g +b)/3)
                # place a pixel from the original image into every pixel of the new image
                new_image.putpixel((x, y), (gray, gray, gray))
    if gray_ask == "2":
        for x in range(width):
            for y in range(height):
                # gets the rgb values for evry single pixel after the iteration is done
                r, g, b = image.getpixel((x, y))
                gray = int((0.299*r) + (0.587*g) + (0.114*b))
                # place a pixel from the original image into every pixel of the new image
                new_image.putpixel((x, y), (gray, gray, gray))

    # open the new image
    new_image.show()

    flip_ask = input("Choose between a vertical flip or a horizontral flip [vertical/horizontal]: ")
    # the transpose function from the image module in the pillow library allows us to flip and rotate the image in 90-degree steps
    if flip_ask == "horizontal":
        # flip the image horizontally
        horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
        horizontal_flip.show()
    if flip_ask == "vertical":
        # flip the image vertically
        vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
        vertical_flip.show()

if __name__ == "__main__":
    main()