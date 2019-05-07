# -*- coding: utf-8 -*-

from app import app,db
from app.models import Todo
from flask import render_template,request


@app.route('/')
def HelloWorld():
    return 'Hello World!'

@app.route('/todo/')
def todo():
    todos = Todo.query.all()
    #return render_template( "index.html",site_name="测试继承" )
    return render_template( "index.html",site_name="测试继承", todos = todos )

@app.route('/add', methods=['POST'])
def add():
    print('请求头：%s' %request.headers )
    print('请求方式：%s' %request.method )
    print('请求url地址：%s' %request.url )
    print('请求数据：%s' %request.data )
    form=request.form
    content = form['content']
    todo = Todo(content=content)
    db.session.add(todo)
    db.session.commit()
    todos = Todo.query.all()
    return render_template( "index.html",site_name="测试继承", todos = todos )

