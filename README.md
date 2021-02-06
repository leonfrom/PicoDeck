# PicoDeck
Turn your Raspberry Pi Pico into a Macro Pad using the [Pico RGB Keypad Base](https://shop.pimoroni.com/products/pico-rgb-keypad-base) from Pimoroni.

## Prequisite
To use this project you have to install CircuitPython on your [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/).
You can download the UF2-File from the [CircuitPython Website](https://circuitpython.org/board/raspberry_pi_pico/).

Push and hold the BOOTSEL button and plug your Pico into the USB port of your Raspberry Pi or other computer. Release the BOOTSEL button after your Pico is connected. It will mount as a Mass Storage Device called RPI-RP2. Drag and drop the CircuitPython UF2 file onto the RPI-RP2 volume. Your Pico will reboot. You are now running CircuitPython.

## Getting Started
Once your Pico is booted you should see a Storage Device called CIRCUITPY. Copy content from the lib folder of this repository to the lib folder of your Pico and replayce the code.py.
The Board should read the new code and from now on you can use the Keypad to trigger actions.

By default each Key triggers the Control-Key and the associated F-Key (F1-F16). While pressing each key will light up with a random colour except the C and F key. I use the C and F key to toggle my microphone and the mute my system sound but you are free to change it.