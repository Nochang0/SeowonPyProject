```
┌─────────────────────────────────────────────────────────────┐
 ____                        __      __                     
/\  _`\                     /\ \  __/\ \                    
\ \,\L\_\      __     ___   \ \ \/\ \ \ \    ___     ___    
 \/_\__ \    /'__`\  / __`\  \ \ \ \ \ \ \  / __`\ /' _ `\  
   /\ \L\ \ /\  __/ /\ \L\ \  \ \ \_/ \_\ \/\ \L\ \/\ \/\ \ 
   \ `\____\\ \____\\ \____/   \ `\___x___/\ \____/\ \_\ \_\
    \/_____/ \/____/ \/___/     '\/__//__/  \/___/  \/_/\/_/
    
     __ __       ______                                  
    /\ \\ \     /\__  _\                                 
    \ \ \\ \    \/_/\ \/     __      __       ___ ___    
     \ \ \\ \_     \ \ \   /'__`\  /'__`\   /' __` __`\  
      \ \__ ,__\    \ \ \ /\  __/ /\ \L\.\_ /\ \/\ \/\ \ 
       \/_/\_\_/     \ \_\\ \____\\ \__/.\_\\ \_\ \_\ \_\
          \/_/        \/_/ \/____/ \/__/\/_/ \/_/\/_/\/_/
                                                     
     ____                                            __      
    /\  _`\                  __                     /\ \__   
    \ \ \L\ \ _ __    ___   /\_\       __     ___   \ \ ,_\  
     \ \ ,__//\`'__\ / __`\ \/\ \    /'__`\  /'___\  \ \ \/  
      \ \ \/ \ \ \/ /\ \L\ \ \ \ \  /\  __/ /\ \__/   \ \ \_ 
       \ \_\  \ \_\ \ \____/ _\ \ \ \ \____\\ \____\   \ \__\
        \/_/   \/_/  \/___/ /\ \_\ \ \/____/ \/____/    \/__/
                            \ \____/                         
                             \/___/                          

└─────────────────────────────────────────────────────────────┘
```

# 🌐 서원대학교 비판적사고 4조 팀 프로젝트

2023년 서원대학교 1학년 2학기 비판적사고(파이썬) 4조 팀 프로젝트 통합 저장소입니다.

## 🗃️ 구성

- **개발 환경**
  - `Visual Studio Code (Windows 10)`
  - `GoormIDE (Ubuntu 18.04.6)`

- **프로젝트 주제:** **유튜브 동영상 다운로드 사이트**

- **팀 구성(3)**
  - **팀장(1):** `연승현(202311420)`
  - **팀원(2):** `박건호(202110501), 홍태민(202311448)`
 
- **기술 스택**
  - **프론트엔드 (Front-End)**
    - HTML
    - CSS
    - JavaScript
  - **백엔드 (Back-End)**
    - Python 3.9.18 (Flask)
    
- **팀 프로젝트 파일 트리**
    ```
    📦 4조 팀 프로젝트
    ┣  📂 lib
    ┃   ┗ 📜 ytdl.h (유튜브 동영상 다운로드 및 관리 라이브러리)
    ┣  📂 static
    ┃	┣  📂 html
    ┃	┃   ┗  📂 main
    ┃	┃	┣  📂 css
    ┃	┃	┃    ┣  📜 fontawesome-all.min.css (UI)
    ┃	┃	┃    ┗  📜 main.css (UI)
    ┃	┃	┃
    ┃	┃	┣  📂 js
    ┃	┃	┃   ┗  📜 main.js (UI)
    ┃	┃	┃
    ┃	┃	┣ 📂 sass
    ┃	┃	┣ 📂 webfonts
    ┃	┃	┗ 📜 index.html (UI)
    ┃	┃	 
    ┃	┗ 📂 media
	┃	    ┣  📄 video.mp4 (다운받은 mp4 파일)
	┃	    ┗  📄 audio.mp3 (다운받은 mp3 파일)
    ┃
    ┃
    ┣ 📄 LICENSE
    ┣ 📄 README.md
    ┗ 💻 main.py (서버 및 실행 파일)
    ```
## ♻️ 역할

- **연승현 (202311420): 프로그램 설계 및 서버 개발, 발표 준비**
- **홍태민 (202311448): UI 설계 및 디자인, 발표 준비 및 발표**
- **박건호 (202110501): YouTube 미디어 관리 라이브러리 개발, 발표 준비 및 발표**

## ✔️ 모임

- **11월 24일(금): 프로젝트 역할 분담 및 개발**
- **12월 1일(금): 발표 준비 및 프로젝트 마무리**

## 💾 유튜브 동영상 다운로드 사이트 개발 프로젝트

- **유튜브 다운로드 홈페이지**
    - Home: https://seowonpy.run.goorm.app/
    - Download URL: https://seowonpy.run.goorm.app/youtube?url={유튜브_영상_URL}&form={파일_형식(mp3|mp4)}
    
- **사용한 라이브러리(Used Library)**
    - `flask`
    - `pytube`
        
- **사용자 정의 라이브러리(User-defined Library)**
    - `ytdl.py`
        
- **라이브러리 소개 및 세부기능**

    - **라이브러리 소개**
        <br>
        | 	라이브러리   |	 	 						소개 							|
        | :----------: | :----------------------------------------------------------------:|
        | flask        | 웹 서버를 개발하기 위한 경량하면서도 간편한 웹 프레임워크                   |
        | pytube       | 파이썬에서 YouTube 동영상을 다운로드하는 데 사용되는 라이브러리      	   	| 
        | ytdl.py      | 커스텀으로 만든 유튜브 영상 다운로드 및 파일이나 영상의 정보를 관리하는 라이브러리|
    
    - **커스텀 라이브러리(ytdl.py) 세부 내용**
        <br>
        | 	클래스 및 함수 (Class Or Function)  | 역할(Role) | 인수(Argument) | 출력 값(Return Value) |
        |:-----------------------------------:|:----------:|:-------------:|:--------------------:|
        | class YTDownloader()   | ytdl.py 라이브러리의 클래스 | X | X |
        | def download(self, url: str, form: str) | YTDownloader 클래스에 속해있고 유튜브 영상을 다운로드하는 함수 | 유튜브 영상링크(str), 다운받을 파일 형식(str) | 영상 이름(str) 또는 False(boolean) |
        <br>

## 🔧 IDE WorkSpace Tip & Guide

* Command feature
	* You can simply run your script using the shortcut icons on the top right.
	* Check out `PROJECT > Common/Build/Run/Test/Find Command` in the top menu.
	

* Useful shortcut
	
| Shortcuts name     | Command (Mac) | Command (Window) |
| ------------------ | :-----------: | :--------------: |
| Copy in Terminal   | ⌘ + C         | Ctrl + Shift + C |
| Paste in Terminal  | ⌘ + V         | Ctrl + Shift + V |
| Search File        | ⌥ + ⇧ + F     | Alt + Shift + F  |
| Terminal Toggle    | ⌥ + ⇧ + B     | Alt + Shift + B  |
| New Terminal       | ⌥ + ⇧ + T     | Alt + Shift + T  |
| Code Formatting    | ⌥ + ⇧ + P     | Alt + Shift + P  |
| Show All Shortcuts | ⌘ + H         | Ctrl + H         |
