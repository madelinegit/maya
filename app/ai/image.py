import requests
from app.config import MODELSLAB_API_KEY, MODELSLAB_IMAGE_URL, MODELSLAB_IMAGE_MODEL


def generate_image(prompt):

    payload = {
    "key": MODELSLAB_API_KEY,
    "model_id":MODELSLAB_IMAGE_MODEL,
    "prompt": prompt,
    "negative_prompt": "bad quality, blurry, distorted, watermark",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "guidance_scale": 7.5,
    "safety_checker": "no",
}

    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post(
        MODELSLAB_IMAGE_URL,
        json=payload,
        headers=headers,
        timeout=60
    )

    data = r.json()
    print("IMAGE API RAW:", data)

    if data.get("status") == "success":
        return data["output"][0]

    if data.get("status") == "processing":
        return data.get("future_links", [None])[0]

    return None