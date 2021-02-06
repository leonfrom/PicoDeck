import time
import board
import busio
import usb_hid

from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from digitalio import DigitalInOut, Direction, Pull

import random


# Prerequisites
#
# Requires Adafruit CircuitPython: https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython
#
# Also requires the following CircuitPython libs: adafruit_hid, adafruit_bus_device, adafruit_dotstar
# (drop them into the lib folder)
#
# Save this code in code.py on your Raspberry Pi Pico CIRCUITPY drive


# Pull CS pin low to enable level shifter
cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0

# Set up APA102 pixels
num_pixels = 16
pixels = adafruit_dotstar.DotStar(board.GP18, board.GP19, num_pixels, brightness=0.5, auto_write=True)

# Set up I2C for IO expander (addr: 0x20)
i2c = busio.I2C(board.GP5, board.GP4)
device = I2CDevice(i2c, 0x20)

# Set up the keyboard
kbd = Keyboard(usb_hid.devices)

# Function to map 0-255 to position on colour wheel
def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def randomColor():
    return(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Read button states from the I2C IO expander on the keypad
def read_button_states(x, y):
    pressed = [0] * 16
    with device:
        # Read from IO expander, 2 bytes (8 bits) correspond to the 16 buttons
        device.write(bytes([0x0]))
        result = bytearray(2)
        device.readinto(result)
        b = result[0] | result[1] << 8

        # Loop through the buttons
        for i in range(x, y):
            if not (1 << i) & b:
                pressed[i] = 1
            else:
                pressed[i] = 0
    return pressed

# List to store the button states
held = [0] * 16

# Init Pixels
pixels[12] = (0, 255, 0)
pixels[15] = (0, 255, 0)

# Keep reading button states, setting pixels
while True:
    pressed = read_button_states(0, 16)

    if pressed[0]:
        if not held[0]:
            #pixels[0] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[0] = randomColor()
            
            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F1)

            # Update held state to prevent retriggering
            held[0] = 1
    elif pressed[1]:
        if not held[1]:
            #pixels[1] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[1] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F2)

            # Update held state to prevent retriggering
            held[1] = 1
    elif pressed[2]:
        if not held[2]:
            #pixels[2] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[2] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F3)

            # Update held state to prevent retriggering
            held[2] = 1
    elif pressed[3]:
        if not held[3]:
            #pixels[3] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[3] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F4)

            # Update held state to prevent retriggering
            held[3] = 1
    elif pressed[4]:
        if not held[4]:
            #pixels[4] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[4] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F5)

            # Update held state to prevent retriggering
            held[4] = 1
    elif pressed[5]:
        if not held[5]:
            #pixels[5] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[5] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F6)

            # Update held state to prevent retriggering
            held[5] = 1
    elif pressed[6]:
        if not held[6]:
            #pixels[6] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[6] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F7)

            # Update held state to prevent retriggering
            held[6] = 1
    elif pressed[7]:
        if not held[7]:
            #pixels[7] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[7] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F8)

            # Update held state to prevent retriggering
            held[7] = 1
    elif pressed[8]:
        if not held[8]:
            #pixels[8] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[8] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F9)

            # Update held state to prevent retriggering
            held[8] = 1
    elif pressed[9]:
        if not held[9]:
            #pixels[9] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[9] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F10)

            # Update held state to prevent retriggering
            held[9] = 1
    elif pressed[10]:
        if not held[10]:
            #pixels[10] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[10] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F11)

            # Update held state to prevent retriggering
            held[10] = 1
    elif pressed[11]:
        if not held[11]:
            #pixels[11] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[11] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F12)

            # Update held state to prevent retriggering
            held[11] = 1
    elif pressed[12]:
        if not held[12]:
            if pixels[12] == (0, 255, 0, 1.0):
                pixels[12] = (255, 0, 0)
            else:
                pixels[12] = (0, 255, 0)

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F13)

            # Update held state to prevent retriggering
            held[12] = 1
    elif pressed[13]:
        if not held[13]:
            #pixels[13] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[13] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F14)

            # Update held state to prevent retriggering
            held[13] = 1
    elif pressed[14]:
        if not held[14]:
            #pixels[14] = colourwheel(0 * 16)  # Map pixel index to 0-255 range
            pixels[14] = randomColor()

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F15)

            # Update held state to prevent retriggering
            held[14] = 1
    elif pressed[15]:
        if not held[15]:
            if pixels[15] == (0, 255, 0, 1.0):
                pixels[15] = (255, 0, 0)
            else:
                pixels[15] = (0, 255, 0)

            # Trigger Key
            kbd.send(Keycode.LEFT_CONTROL, Keycode.F16)

            # Update held state to prevent retriggering
            held[15] = 1
    else:  # Released state
        for i in range(len(pixels)):
            if i not in [12, 15]:
                pixels[i] = (0, 0, 0)
        for i in range(len(held)):
            held[i] = 0

    