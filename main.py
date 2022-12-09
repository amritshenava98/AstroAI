from flask import Flask
from flask import render_template
from flask import requests
import os 
import numpy
import 

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to AstroAI. I have no clue what I am doing.'


app.run(host='0.0.0.0', port=81)
