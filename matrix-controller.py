from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

import time
import sys

def image_viewer():
    image = Image.open('./images/heart.jpg')

    # Configuration for the matrix
    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.gpio_slowdown = 2

    options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

    matrix = RGBMatrix(options = options)

    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.LANCZOS)

    matrix.SetImage(image.convert('RGB'))
    
    try:
        print(" ** Matrix loop \n Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)

def main():
    image_viewer()

if __name__ == "__main__":
    print('*** Starting matrix controller')
    main()