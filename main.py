import asyncio
import os
import requests
import json
import sys
from fastapi import FastAPI, HTTPException
import urllib.parse
import youtube_dl
import uvicorn
import urllib.parse
from fastapi.responses import StreamingResponse
import httpx

app = FastAPI()


@app.get("/")
async def hello(test: str, test2: str):
    if test is not None or test2 is not None:
        return f'{test}\n{str(test2)}'
    else:
        return "good"



@app.get('/youtube')
async def Youtube_Download_API(url: str, form: str):
    try:
        video_info = await youtube_dl.YoutubeDL().extract_info(url, download=False)
        video_title = video_info['title']
        video_type = form
        video_quality = 'best' + ('video' if form == 'mp4' else 'audio')

        response = StreamingResponse(content=await get_video_stream(video_url))
        response.headers['Content-Disposition'] = f'attachment; filename="{urllib.parse.quote(video_title)}.{video_type}"'
        ydl_opts = {
            'format': video_quality,
            'outtmpl': f'{video_title}.{video_type}'
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
        async for chunk in response.aiter_bytes():
            yield chunk
            
            




if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=3000)
    
# python3 main.py
