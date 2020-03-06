from flask import Flask,render_template,request
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy import create_engine

app1=Flask(__name__,template_folder="sign_up")
@app1.route("/")
def sign_up():
    return render_template("index.html")
@app1.route("/index1")
def index1():
    return render_template("index.html")    
@app1.route("/team1")
def team1():
    return render_template("team.html")
@app1.route("/services1")
def services1():
    return render_template("services.html")      
@app1.route("/contact1")
def contact1():
    return render_template("contact.html")                      
if __name__=="__main__":
    app1.debug=True
    app1.run(host="127.0.0.1",port=5000)