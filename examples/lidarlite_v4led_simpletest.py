# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
from adafruit_lidarlite import v4led


# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)

# Default configuration, with only i2c wires
sensor = v4led.LIDARLiteV4LED(i2c)

# sensor = v4led.LIDARLiteV4LED(i2c,
#         configuration=v4led.CONFIG_MAXRANGE)

while True:
    try:
        # We print tuples so you can plot with Mu Plotter
        print((sensor.distance,))
    except RuntimeError as e:
        # If we get a reading error, just print it and keep truckin'
        print(e)
    time.sleep(0.01)  # you can remove this for ultra-fast measurements!
