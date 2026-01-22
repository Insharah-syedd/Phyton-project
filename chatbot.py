import json
import random
import os
import time

# File to save learned answers
knowledge_file = "offline_chatbot_knowledge.json"

# Load knowledge if exists
if os.path.exists(knowledge_file):
    with open(knowledge_file, "r") as f:
        knowledge_base = json.load(f)
else:
    knowledge_base = {
        "hi": ["Hello!", "Hi there!", "Hey! How are you?"],
        "hello": ["Hello!", "Hi there!", "Hey!"],
        "how are you": ["I'm a bot, but I'm doing great! 😊", "I'm fine, thank you!"],
        "your name": ["I'm AlOfflineBot, your friendly offline chatbot 🤖"],
        "joke": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😆",
            "Why did the computer go to the doctor? Because it caught a virus! 😂",
            "Why do Java developers wear glasses? Because they don't C#! 😜"
        ],
        "time": ["The current time is " + time.strftime("%H:%M:%S")],
        "bye": ["Goodbye! Have a nice day! 👋", "See you later!"]
    }

print("🤖 Welcome to AlOfflineBot! Ask me anything. Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if "bye" in user_input:
        print("AlOfflineBot:", random.choice(knowledge_base.get("bye", ["Goodbye!"])))
        break

    # Check if any keyword matches in the knowledge base
    found_answer = False
    for key in knowledge_base:
        if key in user_input:
            answer = random.choice(knowledge_base[key])
            # Update time dynamically
            if key == "time":
                answer = "The current time is " + time.strftime("%H:%M:%S")
            print("AlOfflineBot:", answer)
            found_answer = True
            break

    # If no answer is found, ask the user to teach it
    if not found_answer:
        print("AlOfflineBot: I don't know the answer. Can you teach me? 🤔")
        new_answer = input("Your answer: ")
        knowledge_base[user_input] = [new_answer]
        # Save learned answers for next time
        with open(knowledge_file, "w") as f:
            json.dump(knowledge_base, f, indent=4)
        print("AlOfflineBot: Got it! I will remember that. ✅")

