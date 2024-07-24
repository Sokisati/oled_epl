import Adafruit_SSD1306
from PIL import Image
import time

# Initialize the library (size of the display)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

# Clear display
disp.begin()
disp.clear()
disp.display()

# Load image
image = Image.open('logo.bmp').convert('1')

# Display image
disp.image(image)
disp.display()

time.sleep(10)

# Clear the display
disp.clear()
disp.display()
