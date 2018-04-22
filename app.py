
from flask import Flask, request, jsonify
from pytube_utils import downloadVideo, downloadPlaylist
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/videos/video', methods=['GET', 'POST'])
def videoDispatcher():
    content = request.get_json(force=True)
    for url in content['urls']:
        downloadVideo(url)
    return jsonify({"message":"video downloaded succesfully"})

@app.route('/api/videos/playlist', methods=['GET', 'POST'])
def playlistDispatcher():
    content = request.get_json(force=True)
    for url in content['urls']:
        downloadPlaylist(url)
        return jsonify({"message":"playlist downloaded succesfully"})

if __name__ == '__main__':
    app.run(debug=True)
