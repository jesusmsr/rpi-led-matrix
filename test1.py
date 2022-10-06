import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

try:
    while True:
        print('running')
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit()