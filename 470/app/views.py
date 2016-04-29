from flask import Flask, render_template, request, redirect, flash, url_for 
import parse
from app import app

mainDictionary = []

@app.route('/')
@app.route('/index', methods = ['GET','POST'])
def index():
    global mainDictionary 
    mainDictionary = parse.parse_file()
    
    if request.method == 'POST':
        return redirect(url_for('/results'))
    else:
        return render_template("index.html")

    
    
@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == 'POST':
        name = request.form.get('name', None)
        result = parse.getClass(name, mainDictionary)
        return render_template('results.html',
                        title = 'Results',
                        results = result)
                        
    elif request.method == 'GET':
        return render_template('results.html')
   