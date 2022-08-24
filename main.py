from flask import Flask, send_from_directory
import random

app = Flask(__name__, static_folder='client/dist/assets')


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/dist', 'index.html')


# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/dist', path)


@app.route("/rand")
def hello():
    return str(random.randint(0, 100))


if __name__ == "__main__":
    app.run(debug=True)