# from "mod.py" import YTDownloader
import ytdl


if __name__ == "__main__":
    # 다운로드할 유튜브 영상 URL 입력
    url = input("다운로드할 유튜브 영상 URL을 입력하세요: ")

    # 파일 확장자 선택
    form = input("다운로드할 파일 형식을 입력하세요 (mp3 또는 mp4): ")

    # YouTubeDownloader 클래스의 인스턴스 생성 및 다운로드 수행
    YT = ytdl.YTDownloader()
    YT.download(url, form)
    print("완료")