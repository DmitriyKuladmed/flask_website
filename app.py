from flask import Flask
from flask import render_template
from flask import url_for
from flask_sqlalchemy import *
from datetime import datetime
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(64), unique=True)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.String, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' %self.id

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/myPage')
def myPage():
    return render_template("index.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'This is page ' + name + '-' + str(id)

if __name__ == '__main__':
    app.run(debug=True)
