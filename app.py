from flask import Flask
app = Flask(__name__)
@app.route("/")
def welcome():
    return "Hello word"

@app.route("/home")
def home():
    return "This is home"    


from controller import *
