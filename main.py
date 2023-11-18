import asyncio
import os
import requests
import json
import sys
from fastapi import FastAPI
from fastapi import Response, HTTPException
import urllib.parse
import youtube_dl
import uvicorn

app = FastAPI()


@app.get("/")
async def hello():
    return "Hello goorm!"

@app.get('/youtube')
async def Youtube_Download_API(url: str, type: str, quality: str):
    try:
        video_info = await youtube_dl.YoutubeDL().extract_info(url, download=False)
        video_title = video_info['title']
        video_type = type
        video_quality = quality + ('video' if type == 'mp4' else 'audio')

        response = Response()
        response.headers['Content-Disposition'] = f'attachment; filename="{urllib.parse.quote(video_title)}.{video_type}"'
        ydl_opts = {
            'format': video_type,
            'quality': video_quality,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            video_stream = ydl.extract_info(url, download=False)
            video_url = video_stream['formats'][0]['url']
            response.body = await get_video_stream(video_url)

        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="서버 오류가 발생하였습니다. 다시 시도해주세요.")

async def get_video_stream(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.content

    
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=3000)




