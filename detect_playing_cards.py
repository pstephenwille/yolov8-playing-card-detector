import os

import torch
from flask import jsonify, request
from flask.blueprints import Blueprint
from ultralytics import YOLO
from PIL import Image

cards = Blueprint('cards', __name__)

model_path = './models/best-300.pt'
model = YOLO(model_path)
# tflite_model = YOLO('./models/best-300_saved_model/best-300_float32.tflite')


def convertToTFLite():
    wha = model.export(format='tflite', int8=True, batch=4)
    tflite_model = YOLO('./models/best-300_saved_model/best-300_float32.tflite', task='detect')
    test = tflite_model.predict('/home/stephen/Projects/yolo8/yolo-detect-playing-card/images/hands/test-3-cards.jpg')


convertToTFLite()

@cards.route('/detect-cards', methods=['GET', 'POST'])
def test():
    image_stream = request.files['image']
    img = Image.open(image_stream)
    results = model.predict(img, show_boxes=True)
    names = model.names
    cards = set()

    for r in results:
        for c in r.boxes.cls:
            cards.add(names[int(c)])

    return jsonify({'cards': list(cards)})



@cards.route('/test-image-dir')
def detect_cards():  # put application's code here
    # img = Image.open('./images/clubs/cards-C2-001.jpg')
    images_dir = './images/hands/'
    images = list(map(lambda img: images_dir + '/' + img, os.listdir('images/hands')))
    cards = set()

    for img in images:
        # results = model.predict(img, save=True, save_txt=True, show_boxes=True)
        results = tflite_model.predict(img,  save=True, save_txt=True, show_boxes=True)

        names = model.names
        for r in results:
            for c in r.boxes.cls:
                cards.add(names[int(c)])

    return jsonify({'cards': list(cards)})
