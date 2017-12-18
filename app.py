from flask import Flask,request, jsonify, render_template
import os
import json

app = Flask(__name__)


{
   "status": "OK"
}


@app.route("/")
def principal():
    return jsonify(status='OK')

@app.route("/status")
def docker():
    return jsonify(status='OK')

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
