from flask import Flask
from flask import render_template
import templates


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return 'Hello world'

@app.route('/about')
def about():
    return 'About Us'

@app.route('/myPage')
def myPage():
    return render_template("index.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'This is page' + name + '-' + id

if __name__ == '__main__':
    app.run(debug=True)
