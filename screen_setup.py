

import sys
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

import pimoroni
from inky.auto import auto
inky = auto(ask_user=True, verbose=True)
saturation = 0.5

display_max_width = 600
display_max_height = 448

blank_screen = Image.new("RGBA", (display_max_width, display_max_height), (255, 255, 255, 255))