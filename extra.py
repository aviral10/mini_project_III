# import base64

# with open("newFile.txt", "r") as r:
#     read_data = r.read()
#     s = base64.decodebytes(read_data.encode('utf-8'))
#     with open("image.png", "wb") as w:
#         w.write(s)

# print("Done")
import requests
url = "http://127.0.0.1:5500/"
with requests.get(url) as r:
    print(r.text)