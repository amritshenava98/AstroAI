import os
import json
from flask import jsonify
cohere_key = os.environ['COHERE_API_KEY']

import cohere
co = cohere.Client(cohere_key)

from cohere.classify import Example

examples = [
  Example('You are a good human being', 'uplifting'),
  Example('You are a good at heart', 'uplifting'),
  Example('God bless you', 'uplifting'),
  Example('You deserve to be loved', 'uplifting'),
  Example('Go be great', 'uplifting'),
  Example('I am amazing', 'uplifting'),
  Example('Dont worry, you got this', 'uplifting'),
  Example('Everything is going to work out', 'uplifting'),
  Example('Remember your place in society, fool', 'toxic'),
  Example('SBF', 'toxic'),
  Example('Go fuck yourself', 'toxic'),
  Example('You piece of shit', 'toxic'),
  Example('chutiya', 'toxic'),
  Example('byawarsi', 'toxic'),
  Example('You are disgusting', 'toxic')
]

def detect_sentiment(inputs):
  response = co.classify(
    model="medium",
    inputs=inputs,
    examples=examples,
  )
  print(type(response.classifications))
  print(response.classifications)
  #json_string = json.dumps(response.classifications)
  print(response.classifications[0])
  result = response.classifications[0]
  return result