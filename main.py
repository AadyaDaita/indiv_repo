from flask import render_template, request
import requests, json
from __init__ import app
# create a Flask instance


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("tic_tac_toe_create_task.html")

if __name__ == "__main__":
    app.run(debug=True)