import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import time

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

disp.begin()
disp.clear()
disp.display()

# Create image to draw on
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image
draw.rectangle((0, 0, width, height), outline=0, fill=0)

font = ImageFont.load_default()

# Write some text
text = "Hello, World!"
draw.text((0, 0), text, font=font, fill=255)

# Display image
disp.image(image)
disp.display()

time.sleep(2)

# Clear the display
disp.clear()
disp.display()

