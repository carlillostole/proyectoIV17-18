from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/")
def rutaStatus():
    return jsonify(status='OK')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

