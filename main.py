from flask import Flask, render_template, Response
from components import Camera
from components import Drivetrain
from config.configuration import Config
from sensorplatform.controller import cleanup
import os

config_path = 'config.json'
configuration = Config('config.json').config()

dt = Drivetrain(configuration)

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
    

if __name__ == '__main__':
    try:
        app.run(debug = True, port=80, host='0.0.0.0', threaded = True)
    except Exception as e:
        print("############## FOUND ERRORS. CLEANING UP ################")
        cleanup()
        raise Exception(e)