import os
from flask import Flask, request, render_template, jsonify
import base64
from tensorflow.keras.models import load_model
import numpy as np
from skimage import color, io
from skimage.transform import resize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Setting up the uploads folder
UPLOAD_FOLDER = f'{os.getcwd()}/static/upload'


# App Setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Home Page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template("index.html")

# Keeping track of the uploaded files in the uploads folder
nseed = 10
tot_items = len(os.listdir(UPLOAD_FOLDER))


@app.route('/data', methods=['POST'])
def create_entry():
    global nseed, tot_items

    # POST request
    tot_items = len(os.listdir(UPLOAD_FOLDER))

    print("tot_items: ", tot_items) # logging total files inside uploads folder

    if tot_items >= 3:  # deleting everything if the number of files is greater than 3
        tot_items = 0
        nseed = 10
        items_inside = os.listdir(UPLOAD_FOLDER)
        for ele in items_inside:
            os.remove(UPLOAD_FOLDER + "/" + ele)

    if request.method == 'POST':
        req = request.get_json(force=True)

        # parse data as JSON
        # Decoding the incoming drawn image
        s = base64.decodebytes(req['data'].encode('utf-8'))
        with open("uploads/image.png", "wb") as w:
            w.write(s)

        # Initialize return value to NULL
        ret_val = str("0")

        # Reading and resizing the drawn image
        image = io.imread('uploads/image.png')
        image = color.rgb2gray(image)
        image_resized = resize(image, (28, 28, 1))
        final = 1 - np.array(image_resized)
        final = np.expand_dims(final, axis=0)

        print(final.shape)  # logging final shape of the image

        # Loading our ML model
        model = load_model("models/mnist_trained_99.h5")
        answer = model.predict(final)

        ret_val = answer.argmax()   # This is our Prediction
        print("Prediction: ", ret_val)  # Logging prediction made
        predictions_list = []
        name = ""
        try:
            name = str(nseed)+ ".png"
            nseed+=1
            predictions_list = [round(x*100, 2) for x in answer[0]]
            savePlot(predictions_list, name)
            print(predictions_list)
            conf = predictions_list[ret_val]
            print("Conf: ", conf)   # Log confidence list
        except:
            print("ERROR")

        # Send data to javascript to display accordingly
        p = {"number": str(ret_val), "predictions": predictions_list, "link": name}
        return jsonify(p)
    else:
        message = {'message':'Had some error'}
        return jsonify(message)


def savePlot(ll, name):
    """
    Save the Confidence plot for the predictions
    """
    fig, ax = plt.subplots(nrows=1, ncols=1)  # create figure & 1 axis
    ax.bar([str(x) for x in range(10)], ll, color="#ff660d")
    plt.xlabel('Digits')
    plt.ylabel('Confidence in %')
    plt.title('Confidence Plot for the prediction')
    fig.patch.set_facecolor((240/255, 240/255, 240/255))
    ax.set_facecolor((240/255, 240/255, 240/255))
    xlocs = [i for i in range(10)]
    plt.ylim(0, 109)
    for i, v in enumerate(ll):
        if int(v) != 0:
            plt.text(xlocs[i]-0.20, v + 0.3, str(v)+"%")
    fig.savefig(f'static/upload/{name}')  # save the figure to file
    plt.close(fig)


if __name__ == '__main__':
    app.run(debug=True)
