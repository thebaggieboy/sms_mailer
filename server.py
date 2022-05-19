#from sms_sender import read_lead_file 
from enum import unique
from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate


app = Flask(__name__)             
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)



# Models
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return self.first_name


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return self.message

@app.route("/", methods=["GET", "POST"])                   
def index():                     
    return render_template("index.html")     


@app.route("/convert", methods=["GET", "POST"])                   
def convert():  
    messages = Messages.query.order_by(Messages.id).all()                   
    return render_template("index.html", messages=messages)     


if __name__ == "__main__":        
    app.run(debug=True)                   