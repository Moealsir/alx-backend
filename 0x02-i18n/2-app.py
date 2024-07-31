#!/usr/bin/env python3
"""A basic Flask app.
This app serves as a starting point for a Flask web application.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_locale() -> str:
    """Retrieves the best matching locale for a web page
    based on the user's preferences."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """render the home page"""
    return render_template('2-index.html')


if __name__ == "__man__":
    app.run(host='0.0.0.0', port=5000)
