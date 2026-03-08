from app.config import PERSONA_FILE


def load_persona():

    with open(PERSONA_FILE, "r", encoding="utf-8") as f:
        return f.read()