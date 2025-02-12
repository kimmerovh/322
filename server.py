import os
from flask import Flask, request, jsonify, send_file
import cv2
import numpy as np

app = Flask(__name__)

PHOTO_PATH = "captured_photo.jpg"

@app.route('/accept-cookies', methods=['POST'])
def accept_cookies():
    return jsonify({"message": "Cookies accepted!"})

@app.route('/upload-photo', methods=['POST'])
def upload_photo():
    file = request.files['image']
    nparr = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite(PHOTO_PATH, img)
    return jsonify({"message": "Фото получено!", "photo_url": "/get-photo"})

@app.route('/get-photo', methods=['GET'])
def get_photo():
    return send_file(PHOTO_PATH, mimetype='image/jpeg')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
