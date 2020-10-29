from flask import Flask, request, render_template, jsonify
import base64
from tensorflow.keras.models import load_model
import numpy as np
from skimage import color, io
from skimage.transform import resize

# App Setup
app = Flask(__name__)

# Home Page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template("index.html")


@app.route('/data', methods=['POST'])
def create_entry():
    # POST request

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
            predictions_list = [round(x*100, 2) for x in answer[0]]
            print(predictions_list)
            conf = predictions_list[ret_val]
            print("Confidence: ", conf)   # Log confidence list
        except:
            print("ERROR")

        # Send data to javascript to display data accordingly
        p = {"number": str(ret_val), "predictions": predictions_list, "link": name}
        return jsonify(p)
    else:
        message = {'message': 'Had some error'}     # handling error cases
        return jsonify(message)


# Run the app
if __name__ == '__main__':
    app.run()
