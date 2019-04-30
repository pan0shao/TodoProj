from app import app
from flask import render_template

@app.route('/')
def HelloWorld():
    return 'Hello World!'

@app.route('/todo/')
def todo():
    return render_template( "index.html" )
