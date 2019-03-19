#!/usr/bin/python
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'value of environment variable MYVAR is: %s!\n<br>On host: %s\n' % (os.environ.get('MYVAR', 'None'), os.environ.get('HOSTNAME'))

