import ssd1306
from machine import Pin, I2C

i2c = I2C(scl=Pin(5), sda=Pin(4))
display = ssd1306.SSD1306_I2C(128, 64, i2c) # addr 60


while True:
    display.fill(0)
    display.text("Hello", 10, 10)
    display.text("World", 10, 26)
    display.text('!!!!!!!', 10, 42)
    display.rect(0, 0, 128, 64, 1)
    display.show()



