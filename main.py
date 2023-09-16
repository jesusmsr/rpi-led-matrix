from flask import Flask
import threading
import queue

app = Flask(__name__)
shared_queue = queue.Queue()

@app.route("/")
def home():
    
    return "hola maricon"   


def run_led_matrix():
    import subprocess
    subprocess.run(["python", "matrix-controller.py"])
    
    
led_thread = threading.Thread(target=run_led_matrix, daemon=True)
led_thread.start()

app.run(debug=True)
