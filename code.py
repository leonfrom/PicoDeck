import time
import board
import busio
import usb_hid

from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

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

# Set up Keycodes
keyMod = Keycode.LEFT_CONTROL
key0 = Keycode.F1
key1 = Keycode.F2
key2 = Keycode.F3
key3 = Keycode.F4
key4 = Keycode.F5
key5 = Keycode.F6
key6 = Keycode.F7
key7 = Keycode.F8
key8 = Keycode.F9
key9 = Keycode.F10
key10 = Keycode.F11
key11 = Keycode.F12
key12 = Keycode.F13
key13 = Keycode.F14
key14 = Keycode.F15
key15 = Keycode.F16

# Return random Color
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

def sendKey(mod, key):
    kbd.press(mod, key)
    time.sleep(0.1)
    kbd.release(mod, key)

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
            pixels[0] = randomColor()
            
            # Trigger Key
            sendKey(keyMod, key0)

            # Update held state to prevent retriggering
            held[0] = 1
    elif pressed[1]:
        if not held[1]:
            pixels[1] = randomColor()

            # Trigger Key
            sendKey(keyMod, key1)

            # Update held state to prevent retriggering
            held[1] = 1
    elif pressed[2]:
        if not held[2]:
            pixels[2] = randomColor()

            # Trigger Key
            sendKey(keyMod, key2)

            # Update held state to prevent retriggering
            held[2] = 1
    elif pressed[3]:
        if not held[3]:
            pixels[3] = randomColor()

            # Trigger Key
            sendKey(keyMod, key3)

            # Update held state to prevent retriggering
            held[3] = 1
    elif pressed[4]:
        if not held[4]:
            pixels[4] = randomColor()

            # Trigger Key
            sendKey(keyMod, key4)

            # Update held state to prevent retriggering
            held[4] = 1
    elif pressed[5]:
        if not held[5]:
            pixels[5] = randomColor()

            # Trigger Key
            sendKey(keyMod, key5)

            # Update held state to prevent retriggering
            held[5] = 1
    elif pressed[6]:
        if not held[6]:
            pixels[6] = randomColor()

            # Trigger Key
            sendKey(keyMod, key6)

            # Update held state to prevent retriggering
            held[6] = 1
    elif pressed[7]:
        if not held[7]:
            pixels[7] = randomColor()

            # Trigger Key
            sendKey(keyMod, key7)

            # Update held state to prevent retriggering
            held[7] = 1
    elif pressed[8]:
        if not held[8]:
            pixels[8] = randomColor()

            # Trigger Key
            sendKey(keyMod, key8)

            # Update held state to prevent retriggering
            held[8] = 1
    elif pressed[9]:
        if not held[9]:
            pixels[9] = randomColor()

            # Trigger Key
            sendKey(keyMod, key9)

            # Update held state to prevent retriggering
            held[9] = 1
    elif pressed[10]:
        if not held[10]:
            pixels[10] = randomColor()

            # Trigger Key
            sendKey(keyMod, key10)

            # Update held state to prevent retriggering
            held[10] = 1
    elif pressed[11]:
        if not held[11]:
            pixels[11] = randomColor()

            # Trigger Key
            sendKey(keyMod, key11)

            # Update held state to prevent retriggering
            held[11] = 1
    elif pressed[12]:
        if not held[12]:
            if pixels[12] == (0, 255, 0, 1.0):
                pixels[12] = (255, 0, 0)
            else:
                pixels[12] = (0, 255, 0)

            # Trigger Key
            sendKey(keyMod, key12)

            # Update held state to prevent retriggering
            held[12] = 1
    elif pressed[13]:
        if not held[13]:
            pixels[13] = randomColor()

            # Trigger Key
            sendKey(keyMod, key13)

            # Update held state to prevent retriggering
            held[13] = 1
    elif pressed[14]:
        if not held[14]:
            pixels[14] = randomColor()

            # Trigger Key
            sendKey(keyMod, key14)

            # Update held state to prevent retriggering
            held[14] = 1
    elif pressed[15]:
        if not held[15]:
            if pixels[15] == (0, 255, 0, 1.0):
                pixels[15] = (255, 0, 0)
            else:
                pixels[15] = (0, 255, 0)

            # Trigger Key
            sendKey(keyMod, key15)

            # Update held state to prevent retriggering
            held[15] = 1
    else:  # Released state
        for i in range(len(pixels)):
            if i not in [12, 15]:
                pixels[i] = (0, 0, 0)
        for i in range(len(held)):
            held[i] = 0

    