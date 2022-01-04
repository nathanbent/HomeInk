# These are the scripts from the official GitHub, they allow us to clean the screen and do other things

import time
from inky.auto import auto
from inky.inky_uc8159 import Inky, CLEAN
#from prefs import Prefs
from PIL import Image

inky_display = auto(ask_user=True, verbose=False)  # Sets some internal parameters for the screen
inky = Inky()

display_max_height = inky.height  # Set heights
display_max_width = inky.width

clean_cycles = 1

def create_blank_background(canvas_width, canvas_height):
    blank_background = Image.new("RGBA", (canvas_width, canvas_height), (255, 255, 255, 0))

def inky_clear():  # inky_clear is from the official GitHub, made for the 7 color.  It is the fastest, as well
    global display_max_height
    global display_max_width
    global clean_cycles
    for _ in range(2):
        for y in range(display_max_height - 1):  # For some reason this has to be flipped in order to work
            for x in range(display_max_width - 1):
                inky.set_pixel(x, y, CLEAN)
        inky.show()
        time.sleep(1.0)
        clean_cycles += 1
    print("inky_clean complete!")



def inky_clean():  # inky_clean is from the GitHub for the 3 color, but still works
    global clean_cycles
    cycles = Prefs.inky_clean_cycles_2_clean
    colours = (inky_display.RED, inky_display.BLACK, inky_display.WHITE)
    colour_names = (inky_display.colour, "black", "white")
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    for i in range(cycles):
        print("Cleaning cycle %i\n" % (i + 1))
        for j, c in enumerate(colours):
            print("- updating with %s" % colour_names[j])
            inky_display.set_border(c)
            for x in range(inky_display.WIDTH - 1):
                for y in range(inky_display.HEIGHT - 1):
                    img.putpixel((x, y), c)
            inky_display.set_image(img)
            inky_display.show()
            time.sleep(1)
    clean_cycles = clean_cycles + cycles  # Add the cycle to the count
    print("inky_clear complete")

def inky_cycle():  # This is from the 7 color GitHub and is just inteded to cycle the colors
    colors = ['Black', 'White', 'Green', 'Blue', 'Red', 'Yellow', 'Orange']

    for color in range(7):
        print("Color: {}".format(colors[color]))
        for y in range(inky.height):
            for x in range(inky.width):
                inky.set_pixel(x, y, color)
        inky.set_border(color)
        inky.show()
        time.sleep(5.0)
    print("inky_cycle Complete")

def inky_push_display(image, display_saturation):  # Pushes the display to the screen
    inky.set_image(image, saturation=display_saturation)  # file and saturation level from prefs
    inky.show()  # This is what pushes the display update

def inky_push_display_anysize(image, display_saturation):
    os.system(
        'convert -resize 600x448 -auto-orient ' + image + ' -gravity center -background white -extent 600x448 ' + newimage)  # this uses imagemagick to create a 600x448px image which is ready to be sent to the picture frame
    image = Image.open(newimage)
    inky.set_image(image, saturation=display_saturation)
    inky.show()
