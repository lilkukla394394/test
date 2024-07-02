from flask import Flask, redirect
from random import randint
import time
import threading

app = Flask(__name__)

value_lock = threading.Lock()
value = 1

def randompoint():
    global value
    while True:
        new_value = float(randint(1, 10))
        with value_lock:
            value = new_value
        time.sleep(1)

@app.route('/')
def show_value():
    with value_lock:
        current_value = value
    return str(current_value)

@app.route('/crashpoint')
def redirect_to_discord():
    return redirect("https://discord.gg/fxs68ab6yH")

if __name__ == "__main__":
    threading.Thread(target=randompoint, daemon=True).start()
    app.run(debug=True)
