import os
from pytube import YouTube  # 유튜브 다운로드 라이브러리
from werkzeug.utils import secure_filename  # 파일 이름을 검사하는 라이브러리


class YTDownloader:
    def __init__(self):
        self.output_path = "../static/media/"
        
    def download(self, url: str, form: str):
        try:
            # YouTube 객체 생성
            yt = YouTube(url)

            # 오디오 선택 (form)
            if form == 'mp3':
                #secure_filename(yt.title) + ".mp3"
            
                audio_stream = yt.streams.filter(only_audio=True).first()
                
                # mp3 파일로 변환하여 다운로드
                audio_stream.download(output_path=self.output_path, filename="audio.mp3")
                return "audio.mp3"
            
            # 비디오 선택 (form)
            elif form == 'mp4':
                
                # 가장 높은 화질의 비디오 파일 가져오기
                video_stream = yt.streams.get_highest_resolution()
                audio_stream = yt.streams.filter(only_audio=True).first()

                # 비디오와 오디오를 결합하여 다운로드
                # secure_filename(yt.title) + ".mp4"
                video_stream.download(output_path=self.output_path, filename="video.mp4")
                return "video.mp4"
            
            else:
                print("지원하지 않는 파일 형식입니다.")
                return False

        except Exception as e:
            print(f"다운로드 중 오류 발생: {e}")
            return False