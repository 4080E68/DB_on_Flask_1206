from os import name
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
db = SQLAlchemy(app)

class FileContents(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']

    newFile = FileContents(name = file.filename,data = file.read())
    db.session.add(newFile)
    db.session.commit()

    return render_template("result.html",filename=file.filename)#'<h1> Saved:' + file.filename + 'to the database!</h1>'


if __name__ == '__main__':
    app.run(debug = True)