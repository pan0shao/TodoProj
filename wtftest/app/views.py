from app import app
from flask import render_template, request
from app.models import RegisterationForm,ProfileForm



@app.route('/')
def index():
    return render_template( "index.html" , site_name="ceshi")

@app.route('/wtf',methods=['POST','GET'] )
def tform():
    tforms = RegisterationForm()
    form = request.form
    unm = form['username']
    if unm == 'a':
        message = "success !!"
    return render_template( "index.html" , forms=tforms, messages=message )

