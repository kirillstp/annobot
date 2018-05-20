from flask import Flask, render_template, Response
#from components import Camera
#from components import Drivetrain
import os

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True, port=80, host='0.0.0.0')