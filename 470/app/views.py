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
        #get the data from the form 
        className = request.form.get('className', None)
        classNumber = request.form.get('classNumber', None)
        classInput =  className + "-" + classNumber
        
        #retrive data from "server"
        result = parse.getClass(classInput, mainDictionary)
        
        #check if the input matched a class
        if not result: 
            return render_template('Error.html',
                                    results = classInput)
        else:
            return render_template('results.html',
                            title = 'Results',
                            results = result)
                        
    elif request.method == 'GET':
        return render_template('results.html')
   