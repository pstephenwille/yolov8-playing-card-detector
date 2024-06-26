from flask import Flask
from detect_playing_cards import test_page
app = Flask(__name__)

app.register_blueprint(test_page)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
