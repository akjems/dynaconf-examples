# This file demonstrates Dynaconf having
# an environment variable overwriting a 
# default value.
# export FLASK_VARIABLE="Jim" to greet Jim instead of Ken. 

from flask import Flask
from dynaconf import FlaskDynaconf

app = Flask(__name__)
FlaskDynaconf(
    app, 
    VARIABLE="Ken"
)


@app.route('/')
def hello_world():
    name = app.config["VARIABLE"]
    return f'Hello, {name}!'