import os
from flask import Flask, request, redirect, url_for, render_template, jsonify
import base64
import time
###
from tensorflow.keras.models import load_model
import numpy as np
from skimage import data, color, io
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import math
###

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
        with open("uploads/image.png", "wb") as w:
            w.write(s)

        #####
        ret_val = str("NOPE")

        image = io.imread('uploads/image.png')
        image = color.rgb2gray(image)
        image_resized = resize(image, (28, 28, 1))

        final = ((1 - np.array(image_resized)))


        final = np.expand_dims(final, axis=0)
        print(final.shape)

        model = load_model("models/mnist_trained_99.h5")
        answer = model.predict(final)

        ######
        # plt.imshow(final, cmap='gray')
        # plt.savefig('books_read.png')

        ######
        ret_val = answer.argmax()
        print(ret_val)
        vals = [x for x in answer[0]]
        ll = []
        try:
            ll = [round(x*100) for x in answer[0]]
            print(ll)
            conf = ll[ret_val]
            print("Conf: ", conf)
        except:
            print("ERROR")

        #####
        # return str(ret_val)
        p = {"number": str(ret_val), "predictions": ll}
        return jsonify(p)
    else:
        message = {'message':'Had some error'}
        return jsonify(message)



if __name__ == '__main__':
    app.run(debug=True)
