import time

import board
import led
import mfrc522
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize the keyboard object.
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Setup RGB LED
LED = led.LED(board.GP18, board.GP19, board.GP20)
WHITE = led.Color(15535, 15535, 15535)
BLACK = led.Color(0, 0, 0)

CLOCK = board.GP2
MOSI = board.GP3
MISO = board.GP4
RESET = board.GP5
CHIP_SELECT = board.GP6

rdr = mfrc522.MFRC522(CLOCK, MOSI, MISO, RESET, CHIP_SELECT)
rdr.set_antenna_gain(0x07 << 4)

try:
    while True:

        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:

            (stat, raw_uid) = rdr.anticoll()

            if stat == rdr.OK:
                print("New card detected")
                print("  - tag type: 0x%02x" % tag_type)
                print("  - uid\t : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))

                LED.set(WHITE)

                keyboard_layout.write("%02x%02x%02x%02x\n\n\n" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]), 0.05)

                time.sleep(2)
                LED.set(BLACK)

except KeyboardInterrupt:
    print("Bye")
