# import base64

# with open("newFile.txt", "r") as r:
#     read_data = r.read()
#     s = base64.decodebytes(read_data.encode('utf-8'))
#     with open("image.png", "wb") as w:
#         w.write(s)

# print("Done")
import numpy as np
import pickle
from keras.models import load_model
new_model = load_model("models/mnist_trained_99.h5")
print("ok")
filename = 'models/final.pkl'
pickle.dump(new_model, open(filename, 'wb'))
print("success")