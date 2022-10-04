from flask import Flask
from flask import render_template
from flask import url_for
from flask import request, redirect
from flask_sqlalchemy import *
from datetime import datetime
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.data).all()
    return render_template("posts.html", articles=articles)

@app.route('/create-article', methods=['POST', 'GET'])
def createArticle():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'При создании статьи произошла ошибка'
    else:
        return render_template("create-article.html")


if __name__ == '__main__':
    app.run(debug=True)
