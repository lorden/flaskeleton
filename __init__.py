import os
from flask import Flask


app = Flask(__name__)


def register_blueprints(app):
    from flaskeleton.urls import flaskeleton_urls
    app.register_blueprint(flaskeleton_urls)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
