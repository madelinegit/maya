import requests

from app.config import MODELSLAB_API_KEY, MODELSLAB_API_URL, MODELSLAB_MODEL
from app.ai.memory import get_history, add_message
from app.ai.persona import load_persona


def generate_reply(user_id, message):

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
