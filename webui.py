from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/manual_results')
def manual_results():
    