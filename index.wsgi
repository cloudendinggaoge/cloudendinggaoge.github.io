from bottle import Bottle, run, template

import sae

app = Bottle()

@app.route('/')
def hello():
    return template('index.html')

application = sae.create_wsgi_app(app)