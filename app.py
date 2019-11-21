import os

from flask import Flask

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
  return """<h1 style="color: #256;">Hi mom</h1>"""

@app.route("/hi/<name>")
def hi(name):
  return """<h1 style="color: #256;">Hi """ + name + """</h1>"""

@app.route("/db")
def db():
  return os.environ.get("DATABASE_URL")
