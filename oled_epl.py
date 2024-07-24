import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import time

# Initialize the library (size of the display)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

# Initialize display
disp.begin()
disp.clear()
disp.display()

# Load image
logo = Image.open('logo.bmp').convert('1')

# Display logo
disp.image(logo)
disp.display()
time.sleep(5)

# Create a new image for the text
image = Image.new('1', (128, 64))
draw = ImageDraw.Draw(image)

# Load a font
try:
    font = ImageFont.truetype('DejaVuSans-Bold.ttf', 10)
except IOError:
    font = ImageFont.load_default()

# Define text to display
text_lines = [
    "Sicaklik / Temperature: 30 °C",
    "Basinç / Pressure: 101.325 kPa",
    "Irtifa / Altitude: 55.6",
    "Pil voltaji / Battery voltage: 7.2 V",
    "GPS enlem, boylam, irtifa / GPS lat, long, alt:",
    "38.46833997915811, 27.192330535232344, 46.3"
]

# Position to start drawing text
y = 0

# Draw the text
for line in text_lines:
    draw.text((0, y), line, font=font, fill=255)
    y += 10  # Move down for the next line

# Display the image
disp.image(image)
disp.display()

time.sleep(5)

# Clear the display
disp.clear()
disp.display()
