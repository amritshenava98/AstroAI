from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import make_response
from functions import detect_sentiment
import numpy

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    inputs=[]
    value = request.form['test']
    inputs.append(value)
    result = detect_sentiment(inputs)
    #print(jsonify(result))
    return render_template('home.html', value=value, result=result)
  else:
    return render_template('home.html')


app.run(host='0.0.0.0', port=81)
