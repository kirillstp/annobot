from flask import Flask, render_template, Response, request
import json
from components import Camera
from components import Drivetrain
from components import Headlights
from components import Speaker
from components import IRLED
from config.configuration import Config
from sensorplatform.controller import cleanup
import os

config_path = 'config.json'
configuration = Config('config.json').config()

dt = Drivetrain(configuration)
hl = Headlights(configuration)
spkr = Speaker()
irled= IRLED(configuration)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/drivetrain/forward')
def drivetrain_forward():
    dt.drive_forward()
    return 'OK'

@app.route('/drivetrain/backward')
def drivetrain_backward():
    dt.drive_backward()
    return 'OK'

@app.route('/drivetrain/stop')
def drivetrain_stop():
    dt.stop()
    return 'OK'

@app.route('/drivetrain/turn_left')
def drivetrain_turn_left():
    dt.turn_left()
    return 'OK'

@app.route('/drivetrain/turn_right')
def drivetrain_turn_right():
    dt.turn_right()
    return 'OK'

@app.route('/headlights/toggle')
def headlights_toggle():
    hl.toggle()
    return  Response(json.dumps({
            "state": hl.get_state()
            }), mimetype = u'application/json')

@app.route('/speaker/toggle')
def sound_toggle():
    title=request.args.get('title', default = 1, type = str)
    spkr.toggle(title)
    return  Response(json.dumps({
        "state": spkr.get_state(title)
        }), mimetype = u'application/json')

@app.route('/tv_remote/press')
def tv_remote_press():
    button = request.args.get('button', default="power_test", type = str)
    irled.run_code(button)
    return  "OK"

if __name__ == '__main__':
    try:
        app.run(debug = True, port=80, host='0.0.0.0', threaded = True)
    except Exception as e:
        print("############## FOUND ERRORS. CLEANING UP ################")
        cleanup()
        raise Exception(e)