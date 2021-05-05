import os
from typing import AnyStr

from flask import Flask, request, render_template
from controllers.scanner import image_to_text


def create_app(config_filename):
    """
    App factory
    Args:
        config_filename: Path to config

    Returns:
        app object
    """
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.config.update(SECRET_KEY=os.urandom(24))
    return app


app = create_app("config.py")


@app.route('/', methods=['GET'])
def mainPage():
    return render_template("index.html")


@app.route('/ocr', methods=['POST'])
def scanReceipt() -> AnyStr:
    """
    OCR text detection endpoint
    Returns:
        Extracted text from the image
    """
    r = request
    file = request.files['file']
    lang = request.form['lang'] if 'lang' in request.form.keys() else "eng"
    config = {'lang': lang}
    text = image_to_text(file, config)
    return text
