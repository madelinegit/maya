memory_store = {}


def get_history(user_id):

    if user_id not in memory_store:
        memory_store[user_id] = []

    return memory_store[user_id]


def add_message(user_id, role, content):

    if not content or not content.strip():
        return

    history = get_history(user_id)

    history.append({
        "role": role,
        "content": content
    })

    if len(history) > 10:
        history.pop(0)