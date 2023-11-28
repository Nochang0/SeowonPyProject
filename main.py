import os
import sys
from lib import ytdl
from pytube import YouTube
from werkzeug.utils import secure_filename  # 파일 이름을 안전하게 만들어주는 함수
from flask import Flask, request, send_file, send_from_directory



YT = ytdl.YTDownloader()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return send_from_directory('./static/html/main', 'index.html')


@app.route('/youtube', methods=['GET'])
def download_media():
    # 유튜브 영상 URL과 파일 형식을 받아옴
    url = request.args.get('url')
    form = request.args.get('form')
    
    if not url or not form:
        return "유튜브 링크와 파일 형식을 모두 입력하세요."
    
    filename = YT.download(url, form)

    directory = f"./public/media/{filename}"  # 파일이 위치한 디렉토리 경로
    
    return send_file(directory, as_attachment=True)

    if filename == False:
        return "다운로드에 실패했습니다."
    else:
        return "다운로드에 성공했습니다."

    
@app.route('/test', methods=['GET'])
def hello():
    text = YT.test()
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
