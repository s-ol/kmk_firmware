import board
from busio import I2C
from adafruit_displayio_ssd1306 import SSD1306
from displayio import release_displays, I2CDisplay

from kmk.extensions.rgb import RGB
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.bidirectional import BidirectionalScanner, mapping_left_right


class KMKKeyboard(_KMKKeyboard):
    extensions = [
      RGB(pixel_pin=board.GP11, num_pixels=48+4),
    ]
    col_pins = [board.GP8, board.GP4, board.GP0, board.GP6, board.GP7, board.GP9]
    row_pins = [board.GP5, board.GP1, board.GP2, board.GP3, board.GP10]

    audio_l = board.GP13
    audio_t = board.GP14
    midi_tx = board.GP15
    cv_r = board.GP18
    cv_t = board.GP19

    def __init__(self):
        self.matrix = BidirectionalScanner(
            self.col_pins, self.row_pins, mapping=mapping_left_right
        )

        release_displays()
        i2c = I2C(sda=board.GP14, scl=board.GP15)
        bus = I2CDisplay(i2c, device_address=0x3c)
        self.display = SSD1306(bus, width=128, height=32, rotation=180, auto_refresh=False)


if __name__ == '__main__':
    keyboard = KMKKeyboard()
    keyboard.go()
