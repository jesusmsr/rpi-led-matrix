from flask import Flask
import threading
import queue
import logging
import time
import matrix_controller


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route("/")
def home():
    return "Started server"   

@app.route('/test')
def test():
    print('main')
    try:
        text = 'Lorem ipsum'
        task = {'type': 'test', 'text': text}
        matrix_controller.task_queue.put(task)
        return 'de puta madre'
    except Exception as e:
        return 'oopsie'
    
@app.route('/text')
def text():
    print('main')
    try:
        text = 'Lorem ipsum'
        task = {'type': 'text', 'text': text}
        matrix_controller.task_queue.put(task)
        return 'Works'
    except Exception as e:
        return 'oopsie'

def led_matrix_thread():
    while True:
        time.sleep(1)
        
if __name__ == "__main__":
    print('** Starting')
    led_thread = threading.Thread(target=matrix_controller.main)
    led_thread.daemon = True  # Daemonize the thread so it exits when the main program exits
    led_thread.start()

    app.run(debug=False, host='0.0.0.0')