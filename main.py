import os
import sys
from lib import ytdl
from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS



YT = ytdl.YTDownloader()

app = Flask(__name__)

CORS(app)  # 모든 경로에 대해 CORS를 활성화합니다.

# 메인 다운로드 홈페이지
@app.route('/', methods=['GET'])
def main():
    return send_from_directory('./static/html/main', 'index.html')

# 다운로드 API
@app.route('/youtube', methods=['GET'])
def download_media():
    # 유튜브 영상 URL과 파일 형식을 받아옴 (파라미터)
    url = request.args.get('url')
    form = request.args.get('form')

    if not url or not form:
        return jsonify({ "Error" : "유튜브 링크와 파일 형식을 모두 입력하세요." })

    media = YT.download(url, form)

    directory = "video.mp4" if form == "mp4" else "audio.mp3"  # 파일이 위치한 디렉토리 경로

    return send_file(f"./static/media/{directory}", as_attachment=True, download_name=media)

    if media == False:
        return jsonify({ "Error" : "다운로드에 실패했습니다. 다시 시도해주세요." })
    else:
        return jsonify({ "Error" : "다운로드에 성공했습니다." })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)