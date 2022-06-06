import flask

app = flask.Flask("Lavalink status board")


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/<path:path>")
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
