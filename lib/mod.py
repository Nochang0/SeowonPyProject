from pytube import YouTube
import os
from werkzeug.utils import secure_filename  # 파일 이름을 안전하게 만들어주는 함수

class YTDownloader:
    def __init__(self):
        self.output_path = "../public/media/"

    def test():
        return print("Hello")
    
    def download(self, url: str, form: str):
        try:
            # YouTube 객체 생성
            yt = YouTube(url)

            # 선택한 확장자에 따라 영상 또는 오디오 스트림 선택
            if form == 'mp3':
                audio_stream = yt.streams.filter(only_audio=True).first()
                # mp3 파일로 변환하여 다운로드
                audio_stream.download(output_path=self.output_path, filename=secure_filename(yt.title) + ".mp3")
                print("다운로드 완료!")
                return True
            elif form == 'mp4':
                # 가장 높은 화질의 비디오 스트림과 오디오 스트림 가져오기
                video_stream = yt.streams.get_highest_resolution()
                audio_stream = yt.streams.filter(only_audio=True).first()

                # 비디오와 오디오를 결합하여 다운로드
                video_path = os.path.join(self.output_path, secure_filename(yt.title) + ".mp4")
                video_stream.download(output_path=self.output_path, filename=secure_filename(yt.title) + ".mp4")

                print("다운로드 완료!")
                return True
            else:
                print("지원하지 않는 파일 형식입니다.")
                return False

        except Exception as e:
            print(f"다운로드 중 오류 발생: {e}")
            return False


if __name__ == "__main__":
    # 다운로드할 유튜브 영상 URL 입력
    url = input("다운로드할 유튜브 영상 URL을 입력하세요: ")

    # 파일 확장자 선택
    form = input("다운로드할 파일 형식을 입력하세요 (mp3 또는 mp4): ")

    # YouTubeDownloader 클래스의 인스턴스 생성 및 다운로드 수행
    downloader = YTDownloader()
    downloader.download(url, form)
    
    
    
class yt:
    def __init__(self):
        self.API_KEY = os.getenv('API_KEY')

    async def searchYT(word : str, limit : str):
        try:
            url = f"https://youtube.googleapis.com/youtube/v3/search?fields=nextPageToken,%20items(id/videoId,%20snippet/title,%20snippet/thumbnails/high,%20snippet/channelTitle)&key={self.API_KEY}&maxResults={limit}&pageToken&part=snippet&q={word}&regionCode=kr&type=video"
            response = await requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('items')
        except Exception as e:
            print(e)
            return "오류가 발생했습니다."