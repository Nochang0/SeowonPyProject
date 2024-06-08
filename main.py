# 커스텀 유튜브 라이브러리
from lib import ytdl

# flask 라이브러리에서 호출할 요소들 (클래스, 함수)
from flask import Flask, request, send_file, send_from_directory, jsonify

# CORS를 쉽게 처리하기 위해 사용하는 코드
from flask_cors import CORS


# 커스텀 라이브러리의 클래스 호출
YT = ytdl.YTDownloader()

# flask 라이브러리의 Flask 클래스를 호출
# __name__ : main.py
app = Flask(__name__)
# 포트 설정
port = 3003

# 모든 경로에 대해 CORS(Cross-Origin Resource Sharing)를 활성화합니다.
# 웹 앱에서 발생하는 동일 출처 정책(Same-Origin Policy)을 우회하여 다른 출처의 리소스에 접근할 수 있도록 함
# 동일 출처 정책: 웹 앱에서 다른 출처(프로토콜, 도메인, 포트)의 리소스에 접근하는 것을 제한
# AJAX를 이용하면 웹 페이지의 일부분만을 서버로부터 비동기적으로 요청하고, 해당 부분만을 업데이트할 수 있습니다.
CORS(app)

# 메인 다운로드 홈페이지
@app.route('/', methods=['GET'])
def main():
    # 홈페이지 HTML 파일 경로에 접근해 HTML 코드를 보내줌
    return send_from_directory('./static/html/main', 'index.html')


# 유튜브 다운로드 사이트
@app.route('/youtube', methods=['GET'])
def YouTube_Download_API():
    # 유튜브 영상 URL과 파일 형식을 받아옴 (파라미터)
    # Example: http://localhost:3000/youtube?url=유튜브링크&form=파일형식
    url = request.args.get('url')
    form = request.args.get('form')

    # 유튜브 주소(url) 또는 파일 형식(form)을 입력하지 않았을 떄 오류
    if not url or not form:
        return "유튜브 링크와 파일 형식을 모두 입력하세요."

    # 유튜브 다운로드
    media = YT.download(url, form)
    
    # 다운받은 파일 경로
    filename = "./static/media/video.mp4" if form == "mp4" else "./static/media/audio.mp3"

    # 클라이언트에게 파일 보내주기
    return send_file(filename, as_attachment=True, download_name=media)

    # 다운로드 오류가 발생했을 때
    if media == False:
        return "다운로드에 실패했습니다. 다시 시도해주세요."
    else:
        return "다운로드에 성공했습니다."

# main.py가 직접 실행될 때 실행되어야 하는 코드
if __name__ == '__main__':
    # 서버를 시작하는 코드 (app.run)
    # '0.0.0.0'은 모든 네트워크 인터페이스 (와이파이, 이더넷, 블루투스 등)에서 들어오는 요청을 허용한다는 의미
    app.run(host='0.0.0.0', port=port)