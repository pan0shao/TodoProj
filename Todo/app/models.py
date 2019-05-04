from app import db
import datetime

class Todo(db.Model):
    __tablename__ = 'Todo'
    rid = db.Column(db.Integer, nullable=False, primary_key=True,autoincrement=True )
    content = db.Column(db.String(100) )
    time = db.Column( db.DateTime, default = datetime.datetime.now() )
    status = db.Column(db.Integer, default = 0)

    def __init__(self, content, time=datetime.datetime.now() , status=0 ):
        self.content = content
        self.time = time
        self.status = status

    def __repr__(self):
        return '<Todo %r, time %r, status %r>' % (self.content , self.time ,self.status)
