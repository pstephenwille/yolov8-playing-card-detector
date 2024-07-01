from flask import Flask
from detect_playing_cards import cards
app = Flask(__name__)

app.register_blueprint(cards)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
