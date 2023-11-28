import asyncio
from EdgeGPT import Chatbot, ConversationStyle
from flask import Flask, request
from bardapi import Bard
import os
import requests
import json
import codecs


app = Flask(__name__)
os.environ['_BARD_API_KEY'] = 'awiteZsb71_8knIx2sxEDjC5dgA_cbquaq8eYbROT2yZNYgPiAYO8Q_7DM7mK2Ds1BpAIA.'
BardSession = requests.Session()
BardSession.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
}
# BardSession.cookies.set("__Secure-1PSID", os.environ["_BARD_API_KEY"])
BardSession.cookies.set("__Secure-1PSID", "awiteZsb71_8knIx2sxEDjC5dgA_cbquaq8eYbROT2yZNYgPiAYO8Q_7DM7mK2Ds1BpAIA.")
BardSession.cookies.set("__Secure-1PSIDTS", "sidts-CjEB3e41hZNfl870XSwLSX42XwtYWexHbv1c05417S0WEjfT0Wls8yVhRqpWGwcR-JnUEAA")
BardSession.cookies.set("__Secure-1PSIDCC", "APoG2W8tQO_KWLPqzFAodd3roKXzGEguZUYDbvRcnaa9j-DKS_lnP4qfghb8lWm1EAV5v7-HQpV8")
bard = Bard(session=BardSession, timeout=100)




@app.route("/api/bingai", methods=["GET"])
async def Bing():
    message = request.args.get("word")
    chat = await bingChat(message)
    return chat




@app.route("/api/bard", methods=["GET"])
async def Bard():
    message = request.args.get("word")
    chat = bardChat(message)
    return chat


async def bingChat(msg):
    try:
        bing = await Chatbot.create()
        Bingreply = await bing.ask(prompt=str(msg), conversation_style=ConversationStyle.creative, wss_link="wss://sydney.bing.com/sydney/ChatHub")
        await bing.close()
        return {"result": Bingreply}
    except:
        return {"message": "서버에 오류가 발생하였습니다."}

    
def bardChat(msg):
    try:
        Bardreply = bard.get_answer(str(msg))['content']
        return {"result": msg.encode().decode(Bardreply)}
    except:
        return {"message": "서버에 오류가 발생하였습니다."}
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)