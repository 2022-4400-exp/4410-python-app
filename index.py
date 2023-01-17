from flask import Flask, render_template, request, redirect
from datetime import datetime
import os
app = Flask(__name__)
 
@app.route('/', methods=["GET"])
def index():
    try:
        with open('/var/python-app/data.txt') as f:
            lines = f.read()
    except IOError:
        lines = ""
    return render_template('index.html', data = lines.split("\n"))

@app.route('/', methods=["POST"])
def index_post():

    name = request.form["name"]
    msg = request.form["msg"]
    time = datetime.now()

    with open('/var/python-app/data.txt','a') as f:
    #    f.write(f"{time} {name}「{msg}」\n")
        f.write(f"{time} ひろゆき「論破されました」\n")

    return redirect("/")

if __name__ == '__main__':
    os.makedirs("/var/python-app", exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
