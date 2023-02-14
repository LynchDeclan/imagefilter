# run pip install pillow to install
from PIL import Image

def main():
    # Open image
    image = Image.open('latestart.jpg')

    # Show image
    image.show()

    # get the height and width
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # iterates through all pixels vertical for every horizontal pixel that is being iterated through
    for x in range(width):
        for y in range(height):
            # gets the rgb values for evry single pixel after the iteration is done
            r, g, b = image.getpixel((x, y))
            # place a pixel from the original image into every pixel of the new image
            new_image.putpixel((x, y), (r, 0, 0))

    # open the new image
    new_image.show()

if __name__ == "__main__":
    main()