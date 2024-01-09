# This file demonstrates Dynaconf using
# a settings.toml file for configuration 
# use export FLASK_ENV to set which
# settings to use, for example
# export FLASK_ENV=test

from flask import Flask
from dynaconf import FlaskDynaconf

app = Flask(__name__)
FlaskDynaconf(
    app, 
    settings_file=["settings.toml"]
)


@app.route('/')
def hello_world():
    name = app.config["name"]
    return f'Hello, {name}!'

def name_check():
    return app.config["name"]