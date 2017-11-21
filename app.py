from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/')
def status():
    data={"status":"OK"}
    return json.dumps(data) 


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

