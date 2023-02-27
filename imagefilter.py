# run pip install pillow to install
from PIL import Image
import math
import sys

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



    def grayscale():
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

    def flip():
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

    def Shrinks(new_image, width, height, image):
        width, height = image.size 
        new_width = int((width/2) - (width % 2 ))
        new_height = int((height/2) - (height % 2))
        x2 = 0
        y2 = 0
        shrink_image = Image.new ("RGB", (new_width, new_height), "white")
        
        for x in range(0, width, 2):
            for y in range(0, height, 2):
                try:
                    r1, g1, b1 = image.getpixel((x, y))
                    r2, g2, b2 = image.getpixel((x + 1, y))
                    r3, g3, b3 = image.getpixel((x, y + 1))
                    r4, g4, b4 = image.getpixel((x + 1, y + 1))

                    ave_r = int((r1 + r2 + r3 + r4)/4)
                    ave_g = int((g1 + g2 + g3 + g4)/4)
                    ave_b = int((b1 + b2 + b3 + b4)/4)
                    shrink_image.putpixel((x2, y2), (ave_r, ave_g, ave_b))
                except IndexError:
                    pass

                y2 += 1 
            x2 += 1
            y2 = 0

        shrink_image.show()

    def hide():
        hidden_message = input("What is your hidden message?: ")
        characters = []
        for char in hidden_message:
            characters.append(char)

        for c in characters:
            for x in range(width):
                for y in range(height):
                    bin_red = (bin(r)[2:6])
                    bin_green = (bin(g)[2:6])
                    bin_blue = (bin(b)[2:6])
                    
                    binary_value = (bin(ord(c))[2:6])
                    hidden_red = int(bin_red + binary_value)
                    hidden_green = int(bin_green + binary_value)
                    hidden_blue = int(bin_blue + binary_value)

                    new_image.putpixel((x, y), (hidden_red, hidden_green, hidden_blue))
        
        new_image.show()
                    
    # ask the user what they want to do with this image
    choice_of_function = input(
        "Choose to run (grayscale), (flip), (shrink), or (hide): ")
    if choice_of_function == "grayscale":
        grayscale()
    if choice_of_function == "flip":
        flip()
    if choice_of_function == "shrink":
        Shrinks()
    if choice_of_function == "hide":
        hide()

if __name__ == "__main__":
    main()