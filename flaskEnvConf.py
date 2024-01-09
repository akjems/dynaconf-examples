# This file demonstrates Flask having a default
# set that overwrites environment variables. 
# export FLASK_VARIABLE="Jim" to will greet
# Ken instead of Jim

from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()
app.config["VARIABLE"] = "Ken"
@app.route('/')
def hello_world():
    name=app.config["VARIABLE"]
    return f'Hello, {name}!'