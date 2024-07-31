#!/usr/bin/env python3
"""A basic Flask app.
This app serves as a starting point for a Flask web application.
"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def get_index() -> str:
    """render the home page"""
    return render_template('0-index.html')


if __name__ == "__man__":
    app.run(host='0.0.0.0', port=5000)
