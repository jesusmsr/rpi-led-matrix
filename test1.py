import time
import sys
from samplebase import SampleBase

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

class TestDraw(SampleBase):
    
    def __init__(self, *args, **kwargs):
        super(TestDraw, self).__init__(*args, **kwargs)
    
    def run(self):
        # Configuration for the matrix
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 1
        options.parallel = 1
        options.hardware_mapping = 'adafruit-hat'
        options.gpio_slowdown = 2

        offset_canvas = self.matrix.CreateFrameCanvas()
        
        while True:
            for x in range (0, self.matrix.width):
                offset_canvas.SetPixel(x,x,255,255,255)

# Main function
if __name__ == "__main__":
    test = TestDraw()
    if (not test.process()):
        test.print_help()