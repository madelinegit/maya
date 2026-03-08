import asyncio
import random
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.ai.chat import generate_reply

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(data: dict):
    message = data.get("message")
    reply = generate_reply("default", message)

    await asyncio.sleep(random.uniform(2, 6))

    if random.random() < 0.4 and len(reply) > 80:
        sentences = reply.replace("? ", "?|").replace("! ", "!|").replace(". ", ".|").split("|")
        sentences = [s.strip() for s in sentences if s.strip()]
        if len(sentences) >= 2:
            part1 = sentences[0]
            part2 = " ".join(sentences[1:])
            return {"reply": part1, "followup": part2}

    return {"reply": reply}