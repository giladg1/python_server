# how to run rest service, go to localhost:5000
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello_world():
    return 'Hello everyone'

if __name__ == "__name__":
    app.run()