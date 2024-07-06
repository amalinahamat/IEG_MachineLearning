# flask ia a module
# inside this module we have a class called Flask
# Let us import the class "Flask"
# everytime to run, type =>flask run
from flask import Flask  # type: ignore
# flask run -h 172.16.0.52

app = Flask(__name__) 
#print(__name__)

# if anybody make a http request for "/" then execute
# the following function
# which return Hello World!!! we can see that in hte browser

@app.route("/")
def say_hello():
    return "Hello World!!!"

@app.route("/products")
def get_products():
    
    return ["apple", "vico", "mango"]


