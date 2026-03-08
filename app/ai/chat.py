import requests
import asyncio 
import random

from app.config import MODELSLAB_API_KEY, MODELSLAB_API_URL, MODELSLAB_MODEL
from app.ai.memory import get_history, add_message
from app.ai.persona import load_persona
from app.ai.image import generate_image


def generate_reply(user_id, message):

    lowered = message.lower()

    image_triggers = [
        "show me you", "show me a pic", "show me a photo",
        "show me a picture", "show me what you look like",
        "show me yourself", "let me see you", "can i see you",
        "send me a pic", "send me a photo", "send me a picture",
        "send a pic", "send a photo", "send a picture",
        "drop a pic", "drop a photo", "drop a picture",
        "take a pic", "take a photo", "take a picture",
        "pic of you", "photo of you", "picture of you",
        "what do you look like", "show yourself",
        "post a pic", "post a photo", "post a picture",
        "snap a pic", "snap a photo", "snap a picture",
        "got a pic", "got a photo", "got any pics", "got any photos",
        "see you", "see a pic", "see a photo", "see a picture"
    ]

    if any(phrase in lowered for phrase in image_triggers):
        image_prompt = message.replace("show me", "").replace("send me", "")
        image_prompt = image_prompt.replace("a pic of", "").replace("a photo of", "")
        image_prompt = image_prompt.replace("a picture of", "").strip()

        if len(image_prompt) < 5:
            image_prompt = "Maya, beautiful woman, natural lighting, photorealistic"

        image_url = generate_image(image_prompt)
        if image_url:
            return f"[IMAGE]{image_url}[/IMAGE]"
        else:
            return "I tried to generate an image but something went wrong. Try again!"

    persona = load_persona()
    history = get_history(user_id)

    messages = [{"role": "system", "content": persona}]
    messages.extend(history)

    messages.append({
        "role": "user",
        "content": message
    })

    payload = {
        "model": MODELSLAB_MODEL,
        "messages": messages
    }

    headers = {
        "Authorization": f"Bearer {MODELSLAB_API_KEY}",
        "Content-Type": "application/json"
    }

    r = requests.post(
        MODELSLAB_API_URL,
        json=payload,
        headers=headers,
        timeout=60
    )

    data = r.json()
    print("MODELSLAB RAW:", r.text)

    if "error" in data:
        print("MODEL ERROR:", data)
        return str(data)

    if "choices" in data:
        reply = data["choices"][0]["message"]["content"]
    elif "output" in data:
        reply = data["output"][0]
    else:
        reply = str(data)

    add_message(user_id, "user", message)
    add_message(user_id, "assistant", reply)

    return reply

   