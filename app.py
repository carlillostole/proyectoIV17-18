from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/status')
def status():
    data={"status":"OK"}
    return json.dumps(data) 



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

