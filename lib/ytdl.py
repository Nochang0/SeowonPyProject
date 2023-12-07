from pytube import YouTube  # 유튜브 다운로드 라이브러리


# 추후 기능 추가를 위해 클래스로 라이브러리 구현
class YTDownloader:
    def __init__(self):
        self.output_path = "./static/media/"

    def download(self, url: str, form: str):
        try:
            # pytube 라이브러리의 YouTube 클래스 불러오기
            yt = YouTube(url)

            # 오디오 선택 (form)
            if form == 'mp3':

                # 동영상에서 오디오만 다운받도록 설정
                AudioYT = yt.streams.filter(only_audio=True).first()

                # 영상의 오디오 파일(MP3) 다운로드
                AudioYT.download(output_path=self.output_path, filename="audio.mp3")
                return yt.title + ".mp3"

            # 비디오 선택 (form)
            elif form == 'mp4':

                # 가장 높은 화질의 비디오를 다운받도록 설정
                VideoYT = yt.streams.get_highest_resolution()

                # 비디오와 오디오를 결합하여 다운로드
                VideoYT.download(output_path=self.output_path, filename="video.mp4")
                return yt.title + ".mp4"
            
            # 에러 (Error)
            else:
                print("지원하지 않는 파일 형식입니다.")
                return False

        except Exception as e:
            print(f"다운로드 중 오류 발생: {e}")
            return False