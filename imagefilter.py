# run pip install pillow to install
from PIL import Image
import math
import sys

def main():
    # Opens an image
    image = Image.open('nightbee.png')

    # gets the width and height of the image
    width, height = image.size

    # get the rgb values of a pixel at a certain coordinate
    r, g, b = image.getpixel((50, 50))
    
    # create a new image of the same size as the original
    new_image = Image.new("RGB", (image.size), "white")

    # variable that asks the user whether they want to hide an image or a message
    func_choice1 = input("Do you wish to hide a message? [yes/no]: ")
    func_choice2 = input("Do you wish to hide an image? [yes/no]: ")
    
    # ask the user what they want to do with this image
    choice_of_function = input("Choose to run (grayscale), (flip), (shrink), or (hide): ")

    if choice_of_function == "grayscale":
        grayscale()
    if choice_of_function == "flip":
        flip()
    # if choice_of_function == "shrink":
        # shrink()
    if choice_of_function == "hide":
        image.show()
        hide(image, width, height, func_choice1, func_choice2)
    



def grayscale():
    image = Image.open('nightbee.png')
    width, height = image.size
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

def flip():
    image = Image.open('nightbee.png')
    width, height = image.size
    new_image = Image.new("RGB", (image.size), "white")
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

# def shrink():


def hide(image, width, height, func_choice1, func_choice2):
    # creates a new image that is the same size as the old one, gets rgb format, and makes it pure white
    new_image = Image.new("RGB", (image.size), "white")
    new_image2 = Image.new("RGB", (image.size), "white")
    

    if func_choice1 == "yes":
        # asks the user for their hidden message
        hidden_message = input("What is your hidden message?: ")
        # defines an empty array
        characters = []
        # add every individual character of the hidden message into the empty array
        for char in hidden_message:
            characters.append(char)

        # gets a characters for each pixel.
        for x in range(width):
            for y in range(height):
                for c in characters:
                    # gets the rgb values for each pixel.
                    r, g, b = image.getpixel((x, y))
                    # gets the first four binary values of the red rgb value as a string.
                    bin_red = (bin(r)[2:6])
                    # gets the first four binary values of the green rgb value as a string.
                    bin_green = (bin(g)[2:6])
                    bin_blue = b
                    # converts the ASCII values of the character into a binary string.
                    bin_letter_value = (bin(ord(c)))
                    # gets the first half of the character's bvinary value.
                    firsthalf_character_value1 = ( bin_letter_value[2:6])
                    # gets the second half of the character's bvinary value.
                    firsthalf_character_value2 = ( bin_letter_value[7:10])
                    # adds the first half of the binary character value to the binary red value.
                    hidden_red = int(bin_red + firsthalf_character_value1)
                    # adds the second half of the binary character value to the binary green value.
                    hidden_green = int(bin_green + firsthalf_character_value2)
                    # put in the new rgb values into the new image in the same position as they were in the old image.
                    new_image.putpixel((x, y), (hidden_red, hidden_green, bin_blue))
                    # checks whether the algorithm has iterated over the last character
                    if c == characters[-1]:
                        # iterates through all pixels vertical for every horizontal pixel that is being iterated through
                        for x in range(width):
                            for y in range(height):
                                # gets the rgb values for evry single pixel after the iteration is done
                                r, g, b = image.getpixel((x, y))
                                # puts a new pixel back into the new image in the same position
                                new_image.putpixel((x, y), (r, g, b))
                        new_image.show()
                        sys.exit()
    
    if func_choice2 == "yes":
        print("Here are your choices:\n")
        # gives image choices
        print("buster.png\nhorse.jpg\nhyena.jpg\njump.jpeg\nkitty.png\nlatestart.jpg\nnightbee.png\nowlbear.jpg\nphilip.jpg\nthanksgiving.jpg\n")
        # asks the user for the image that they want to hide in the original
        hidden_image = input("What is your choice of image to hide?: ")
        # defines this chosen image as "image2"
        image2 = Image.open(hidden_image)
        # gets a new width and height for the chosen image
        width2, height2 = image2.size
        # goes through every pixel from the original image
        for x in range(width):
            for y in range(height):
                # goes through every pixel of the new image, putting it inside of the old image
                for x2 in range(width2):
                    for y2 in range(height2):
                        # gets the rgb values for each pixel
                        r,g,b = image.getpixel((x, y))
                        r2,g2,b2 = image2.getpixel((x2, y2))
                        # gets the first four binary values of the red rgb value as a string
                        bin_red1 = (bin(r)[2:6])
                        # gets the first four binary values of the green rgb value as a string
                        bin_green1 = (bin(g)[2:6])
                        # gets the first four binary values of the blue rgb value as a string
                        bin_blue1 = (bin(b)[2:6])
                        # gets the first four binary values of the second image's red rgb value
                        bin_red2 = (bin(r2)[2:6])
                        # gets the first four binary values of the second image's green rgb value
                        bin_green2 = (bin(g2)[2:6])
                        # gets the first four binary values of the second image's blue rgb value
                        bin_blue2 = (bin(b2)[2:6])
                        # adds the first half of the first binary rgb values to the first half of the second binary rgb values
                        hidden_red = int(bin_red1 + bin_red2)
                        hidden_green = int(bin_green1 + bin_green2)
                        hidden_blue = int(bin_blue1 + bin_blue2)
                        # put in the new rgb values into the new image in the same position as they were in the old image
                        new_image2.putpixel((x, y), (hidden_red, hidden_green, hidden_blue))
                        if str(x2) == (str(width2)[-1]) and str(y2) == (str(height2)[-1]):
                            for x in range(width):
                                for y in range(height):
                                    # gets the rgb values for evry single pixel after the iteration is done
                                    r, g, b = image.getpixel((x, y))
                                    # puts a new pixel back into the new image in the same position
                                    new_image2.putpixel((x, y), (r, g, b))
                            new_image2.show()
                            sys.exit()


        

                    
                    


if __name__ == "__main__":
    main()