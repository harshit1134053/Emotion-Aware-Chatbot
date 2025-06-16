import json
from collections import defaultdict

user_memory = defaultdict(list)

def update_memory(user_id, message, reflection):
    user_memory[user_id].append({"input": message, "output": reflection})


def fetch_context(user_id):
    history = user_memory[user_id][-5:]  # last 5 exchanges
    return " | ".join([pair['input'] for pair in history]) if history else ""