from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/k2/api/test-fe.html')
def hello_world() -> 'html':
    return render_template('base.html'
                            )

@app.route('/k2/recommend')
def get_name() -> str:
    return 'gwesley' + random.choice('abcdefg&#%^*f')