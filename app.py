from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/arjundb'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(50))
    
@app.route('/')
@app.route('/ind')

@app.route('/<name>')
def index(name):
    user= User(name=name)
    db.session.add(user)
    db.session.commit()
    return '<h1>Arjun</h1><p>learn more be smart</p>'

if __name__=='__main__':
    app.run(debug=True)
    
app.run(host='0.0.0.0', port=81)