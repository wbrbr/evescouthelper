from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/wormholes")
def wormholes():
    r = requests.get('https://eve-scout.com/api/wormholes')
    return r.text, 200, {'Content-Type': 'application/json'}