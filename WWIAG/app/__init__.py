#!/usr/local/bin/python
# latin-1

import os
from flask import Flask 

app = Flask(__name__)
app.debug = True
app.config.from_object('config')

from app import views
