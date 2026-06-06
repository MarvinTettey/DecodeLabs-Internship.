print("🤖 DecodeBot v2.0")
print("Bot: Hello! I'm DecodeBot.")
print("Bot: What's your name?")

name = input("You: ")

print(f"Bot: Nice to meet you, {name}!")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' anytime to exit.\n")

while True:
    user = input(f"{name}: ").lower()

    if user in ["hello", "hi", "hey"]:
        print(f"Bot: Hello {name}! 😊")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "who created you":
        print("Bot: I was created by Marvin during the DecodeLabs AI Internship.")

    elif user == "what can you do":
        print("Bot: I can chat, tell jokes, answer simple questions, and greet you!")

    elif user == "joke":
        print("Bot: Why did the programmer quit his job?")
        print("Bot: Because he didn't get arrays. 😄")

    elif user == "favorite language":
        print("Bot: Python, of course! 🐍")

    elif user == "help":
        print("\nAvailable Commands:")
        print("- hello")
        print("- how are you")
        print("- joke")
        print("- favorite language")
        print("- who created you")
        print("- what can you do")
        print("- bye\n")

    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a great day. 👋")
        break

    else:
        print("Bot: Hmm... I don't know how to respond to that.")