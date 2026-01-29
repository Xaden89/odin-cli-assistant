import json
import os

MEMORY_FILE = "memory.json"

# Load memory safely
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

# Save memory safely
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

memory = load_memory()

print("Odin is online.")

# Main loop
while True:
    question = input("Ask me something (or type 'quit'): ").strip().lower()

    if question == "quit":
        print("Goodbye.")
        break

    elif question == "who am i":
        name = memory.get("user_name")
        if name:
            print(f"You are {name}.")
        else:
            print("I don't know your name yet.")

    elif question.startswith("remember that my name is"):
        name = question.replace("remember that my name is", "").strip().title()
        memory["user_name"] = name
        save_memory(memory)
        print(f"I will remember that your name is {name}.")

    elif question.startswith("remember that my"):
        parts = question.replace("remember that my", "").split(" is ")
        if len(parts) == 2:
            key, value = parts
            memory[key.strip()] = value.strip()
            save_memory(memory)
            print(f"I will remember that your {key.strip()} is {value.strip()}.")
        else:
            print("I couldn't understand that.")

    elif question.startswith("what is my"):
        key = question.replace("what is my", "").strip()
        if key in memory:
            print(f"Your {key} is {memory[key]}.")
        else:
            print(f"I don't know your {key} yet.")

    else:
        print("I don't understand yet.")
