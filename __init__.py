from flask import Flask
import threading
import time
#import SampleGenerators
from .SampleGenerators import SolidGenerator
from .SampleGenerators import SolidPulse
from .opc import Client

client = Client('localhost:7890')

app = Flask(__name__)

# Pixel Dimensions of the Display
width = 5
height = 1

generator = SolidGenerator(width, height, (255,0,255))

@app.route('/')
def index():
    global generator
    return "Hello, World!"

@app.route('/blue')
def blue():
    global generator
    generator = SolidGenerator(width, height, (0,0,255))
    return "blue"

@app.route('/pulse')
def pulse():
    global generator
    generator = SolidPulse(width, height, (80,255,100))
    return "Pulsing"

def background():
    global generator

    while True:
        #print(generator.next_frame())
        frame = generator.next_frame()
        #print(frame)
        client.put_pixels(frame, channel=0)
        time.sleep(1./10)

t = threading.Thread(target=background)
t.start()
 
