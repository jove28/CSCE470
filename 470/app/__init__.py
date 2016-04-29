#!/usr/local/bin/python
# latin-1
from flask import Flask, session

#conguration 
DEBUG = True
SECRET_KEY = 'development key'


app = Flask(__name__)
app.config.from_object(__name__)

from app import views