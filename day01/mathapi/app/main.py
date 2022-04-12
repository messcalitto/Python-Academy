from flask import Flask, request
from . blueprints import math_bp

def hello_world_json():
    return {"hello": "world", "Project": "Math API"}

app = Flask(__name__)
app.register_blueprint(math_bp, url_prefix="/math")
app.add_url_rule("/", view_func=hello_world_json)
