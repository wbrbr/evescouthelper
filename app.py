from flask import Flask, render_template, jsonify
from tripwire import Tripwire
import os
app = Flask(__name__)
trpw = Tripwire(os.environ['TRIPWIRE_USER'], os.environ['TRIPWIRE_PASS'])

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/wormholes")
def wormholes():
    return jsonify(trpw.load_signatures()), 200, {'Content-Type': 'application/json'}