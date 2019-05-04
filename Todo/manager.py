from app import app,db
from app.models import Todo
from flask_script import Manager

manager = Manager(app)

@manager.command
def CreateTable():
    db.create_all() # 创建所有未创建的table

@manager.command
def save( ):
    #todo = Todo(content="study flask", time=datetime.datetime.now(), status=0 )
    todo = Todo(content="study flask1" )
    db.session.add(todo)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
