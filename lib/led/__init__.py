"""
For use with Pimoroni Tiny 2040.
Color cycles the built-in RGB LED.

Source: https://gist.github.com/mixolydianpink/c516bcf88beca4380e614d47ee74b49b
"""

import time

import board
from microcontroller import Pin
from pwmio import PWMOut

UINT16_MAX = 65535


class Color:
    """
    A color as an RGB triple of integers between 0 and 65535 (uint16).
    """

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self) -> str:
        return f"Color({self.r}, {self.g}, {self.b})"

    def normalized(self):
        """
        Return the color scaled such that one of the channels is at (near) max value.
        """
        maximum = max([self.r, self.g, self.b])
        if maximum == 0:
            return Color(UINT16_MAX, UINT16_MAX, UINT16_MAX)
        else:
            return Color(
                int(UINT16_MAX / maximum * self.r),
                int(UINT16_MAX / maximum * self.g),
                int(UINT16_MAX / maximum * self.b),
            )


class LED:
    def __init__(self, r: Pin, g: Pin, b: Pin) -> None:
        # The Tiny 2040 LED is active low. Full duty is off.
        self.r = PWMOut(r, frequency=5000, duty_cycle=UINT16_MAX)
        self.g = PWMOut(g, frequency=5000, duty_cycle=UINT16_MAX)
        self.b = PWMOut(b, frequency=5000, duty_cycle=UINT16_MAX)

    def set(self, color: Color) -> None:
        # The Tiny 2040 LED is active low. Full duty is off.
        self.r.duty_cycle = UINT16_MAX - color.r
        self.g.duty_cycle = UINT16_MAX - color.g
        self.b.duty_cycle = UINT16_MAX - color.b

    def __enter__(self):
        return self

    def __exit__(self, e_type, e_value, traceback) -> bool:
        self.r.deinit()
        self.g.deinit()
        self.b.deinit()
        return False
