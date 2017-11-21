from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/")
def rutaStatus():
    return jsonify(status='OK')

#@app.route("/status")
#def rutaStatus():
#    return jsonify(status='OK')

#@app.route('/')
#def index():
#    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

