# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/results', methods=['GET', 'POST'])
def results():
    user_element = request.form["user_element"]
    user_pokemon = model.favorite_element(user_element)
    return render_template("results.html", user_pokemon = user_pokemon)