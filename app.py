import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
import base64
import time

UPLOAD_FOLDER = f'{os.getcwd()}/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template("index.html")


@app.route('/data', methods=['POST'])
def create_entry():

    # POST request
    if request.method == 'POST':
        # print('Incoming..')
        req = request.get_json(force=True)
        # print(req)  # parse as JSON

        s = base64.decodebytes(req['data'].encode('utf-8'))
        with open("image.png", "wb") as w:
            w.write(s)
        time.sleep(5)
        return 'WoW'
    else:
        message = {'message':'Had some error'}
        return jsonify(message)



if __name__ == '__main__':
    app.run(debug=True)
