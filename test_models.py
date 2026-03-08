import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MODELSLAB_API_KEY")

url = f"https://modelslab.com/api/v7/models?key={API_KEY}"

response = requests.get(url)

print("\n===== AVAILABLE MODELS =====\n")
print(response.json())
print("\n============================\n")