from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")


    return """
    <h1>Heroku desplegado correctamente</h1>
    <h2>Status heroku: OK</h2>
    <a href="tg://resolve?domain=carlillostole_weatherBot">Acceso al bot de telegram</a>

    <p>It is currently {time}.</p>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

