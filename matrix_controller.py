from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

import time
import sys

import queue
import threading
import time

import logging
from rgbmatrix import graphics

logging.basicConfig(level=logging.DEBUG)

task_queue = queue.Queue()

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.gpio_slowdown = 2
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
matrix = RGBMatrix(options = options)

# Displays a static image
def show_image():    
    image = Image.open('./images/heart.jpg')
    # Make image fit our screen.
    image.thumbnail((matrix.width, matrix.height), Image.LANCZOS)

    matrix.SetImage(image.convert('RGB'))
    
    try:
        print(" ** Matrix loop \n Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)

# Displays moving text
def show_text(text):
    print('TEXT')
    
    offscreen_canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("./fonts/7x13.bdf")
    textColor = graphics.Color(255, 255, 0)
    pos = offscreen_canvas.width

    while True:
        offscreen_canvas.Clear()
        len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, text)
        pos -= 1
        if (pos + len < 0):
            pos = offscreen_canvas.width

        time.sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

def testQueue(msg):
    print('TEST')

def led_matrix_thread():
    while True:
        print('** Checking task queue')
        try:
            task = task_queue.get(timeout=1)  

            if task.get('type') == 'test':
                text = task.get('text')
                show_image()
                
            if task.get('type') == 'text':
                text = task.get('text')
                print('TEXT called')
                show_text(text)
                
            # Mark the task as done
            task_queue.task_done()
        except queue.Empty:
            pass
        
        
    

def main():
    print('*** Starting matrix controller')
    
    
    led_thread = threading.Thread(target=led_matrix_thread)
    led_thread.daemon = True
    led_thread.start()
    