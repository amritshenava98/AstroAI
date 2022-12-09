from flask import Flask
from flask import render_template
from flask import request
import os 
import numpy

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


app.run(host='0.0.0.0', port=81)
