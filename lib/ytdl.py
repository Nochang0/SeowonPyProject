from dotenv import load_dotenv
import requests
import os
import asyncio

load_dotenv()

class ytdl:
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


