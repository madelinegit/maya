import os
from dotenv import load_dotenv

load_dotenv()

MODELSLAB_API_KEY = os.getenv("MODELSLAB_API_KEY")
MODELSLAB_MODEL = os.getenv("MODELSLAB_MODEL")
MODELSLAB_API_URL = os.getenv("MODELSLAB_API_URL")

PERSONA_FILE = "persona/maya.txt"
DATABASE_PATH = "data/maya.db"