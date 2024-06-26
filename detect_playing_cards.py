import os

from flask import jsonify
from flask.blueprints import Blueprint
from ultralytics import YOLO

test_page = Blueprint('test', __name__)

model_path = '/home/stephen/Projects/yolo8/playing-card-detection-yolov8/trained-models/runs-100-gpu/best.pt'
model = YOLO(model_path)


@test_page.route('/test')
def test_hello_world():  # put application's code here
    # img = Image.open('./images/clubs/cards-C2-001.jpg')
    images_dir = './images/diamonds/'
    images = list(map(lambda img: images_dir + '/' + img, os.listdir('./images/diamonds')))
    cards = set()

    for img in images:
        results = model.predict(img, save=True, save_txt=True, show_boxes=True)
        names = model.names

        for r in results:
            for c in r.boxes.cls:
                cards.add(names[int(c)])

    return jsonify({'cards': list(cards)})
