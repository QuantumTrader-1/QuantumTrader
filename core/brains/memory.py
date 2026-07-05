import json
import os

MEMORY_FILE = "core/data/memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(coin, data):

    memory = load_memory()

    history = memory.get(coin, [])

    history.append({
        "price": data["price"],
        "change": data["change"]
    })

    # Keep only the newest 100 observations
    history = history[-100:]

    memory[coin] = history

    save_memory(memory)


def recall(coin):

    memory = load_memory()

    return memory.get(coin, [])