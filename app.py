from flask import Flask, abort, redirect
from flask_mongoengine import MongoEngine

import extensions
from models import Forward

app = Flask(__name__)

import config
app.config.from_object(config)
extensions.init_app(app)

import admin

@app.route("/", defaults={"path": "/"})
@app.route("/<path:path>")
def do_forward(path):
    # look up path in mongo
    # return redirect(mongo url)
    forward = Forward.objects(source=path).first()
    if forward:
        return redirect(forward.dest)
    else:
        abort(404)


if __name__ == "__main__":
    app.run()
