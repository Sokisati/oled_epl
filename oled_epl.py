# -*- coding: utf-8 -*-

import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import time

class OLEDPage:
    def __init__(self):
        self.actionSecond = 6

class BMPPage(OLEDPage):
    def __init__(self, path):
        super().__init__()
        self.bmp = Image.open(path).convert('1')

    def display(self, disp):
        disp.image(self.bmp)
        disp.display()
        time.sleep(self.actionSecond);

class TextPage(OLEDPage):
    def __init__(self, fontSize, textLines):
        super().__init__()
        self.fontSelection = 'DejaVuSans-Bold.ttf'
        self.fontSize = fontSize
        self.font = ImageFont.truetype(self.fontSelection, self.fontSize)
        self.textLines = textLines

    def drawText(self):
        
        image = Image.new('1', (128, 64))
        draw = ImageDraw.Draw(image)
        
        y = 0
        for line in self.textLines:
            draw.text((0, y), line, font=self.font, fill=255)
            y += self.fontSize
        
        return image

    def display(self, disp):
        image = self.drawText()
        disp.image(image)
        disp.display()
        time.sleep(self.actionSecond);

class OLED:
    def __init__(self):
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)
        self.disp.begin()
        self.disp.clear()
        self.disp.display()

    def display(self, page):
        page.display(self.disp)

    def cleanup(self):
        self.disp.clear()
        self.disp.display()


oled = OLED()


bmp_page = BMPPage('logo.bmp')
text_lines = [
    "Sicaklik: 30 C",
    "Basinc: 101.325 kPa",
    "Irtifa: 55.6",
    "Pil voltaji: 7.2 V",
    "Hata kodu listesi:",
    "N/A , N/A , 0 , 1 , N/A"
]
text_page = TextPage(10, text_lines)

oled.display(bmp_page)
oled.display(text_page)



oled.cleanup()
