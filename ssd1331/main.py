import machine
from ssd1331_16bit import SSD1331 as SSD


def setup():
    pdc = machine.Pin(4, machine.Pin.OUT, value=0)
    pcs = machine.Pin(15, machine.Pin.OUT, value=1)
    prst = machine.Pin(5, machine.Pin.OUT, value=1)
    hspi = machine.SPI(1, baudrate=80000000, polarity=0, phase=0)
    return SSD(hspi, pcs, pdc, prst)


ssd = setup()
ssd.fill(0)
x = 0


for y in range(96):
    red = ssd.rgb(round(255 * y / 96), 0, 0)
    green = ssd.rgb(0, round(255 * y / 96), 0)
    blue = ssd.rgb(0, 0, round(255 * y / 96))
    yellow = ssd.rgb(round(255 * y / 96), round(255 * y / 96), 0)
    orange = ssd.rgb(round(255 * y / 96), round(68 * y / 96), 0)
    purple = ssd.rgb(round(179 * y / 96), 0, round(255 * y / 96))
    turquoise = ssd.rgb(0, round(255 * y / 96), round(255 * y / 96))

    ssd.line(y, x, y, x + 10, red)
    ssd.line(y, x + 10, y, x + 20, green)
    ssd.line(y, x + 20, y, x + 30, blue)
    ssd.line(y, x + 30, y, x + 40, yellow)
    ssd.line(y, x + 40, y, x + 50, orange)
    ssd.line(y, x + 50, y, x + 60, purple)
    ssd.line(y, x + 60, y, x + 70, turquoise)

ssd.text("hello!", round(96 / 3), round(96 / 3), ssd.rgb(0, 0, 0))
ssd.show()
