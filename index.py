import requests
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def main():
    return 'Api is working'

@app.route('/<string:topic>')
def playonyoutube(topic):
    url='https://pywhatkit.herokuapp.com/playonyt?topic='+topic
    request=requests.get(url)
    return(request.text)

if __name__ == '__main__':
  app.run()
