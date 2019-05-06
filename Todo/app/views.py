from app import app
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

@app.route('/add', methods=['POST',])
def add():
    content = form[content]
    todo = Todo(content=content)
    db.session.add(todo)
    db.session.commit()
