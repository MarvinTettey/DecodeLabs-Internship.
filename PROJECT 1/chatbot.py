# Decode Labs - Artificial Intelligence Project 1
# Rule-Based AI Chatbot
# Developed by: Marvin Tettey

from datetime import datetime

print("=" * 50)
print("🤖 Welcome to DecodeBot!")
print("I am a Rule-Based AI Chatbot.")
print("Type 'help' to see what I can do.")
print("Type 'exit', 'bye', or 'quit' to end the chat.")
print("=" * 50)

while True:
    user_input = input("\nYou: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
        print("DecodeBot: Hello! Nice to meet you. How can I help you today?")

    # Asking the chatbot's name
    elif user_input in ["what is your name", "who are you", "your name"]:
        print("DecodeBot: My name is DecodeBot. I was created as part of a Decode Labs AI project.")

    # Asking how the chatbot is
    elif user_input in ["how are you", "how are you doing"]:
        print("DecodeBot: I'm doing great! Thanks for asking. How can I assist you?")

    # Help command
    elif user_input == "help":
        print("\nDecodeBot: Here are the things I can do:")
        print("• Greetings (hi, hello, hey)")
        print("• Ask me my name")
        print("• Respond to 'how are you'")
        print("• Explain what AI is")
        print("• Tell the current time")
        print("• Explain what a chatbot is")
        print("• Exit the conversation")

    # AI questions
    elif user_input in ["what is ai", "define ai", "tell me about ai"]:
        print("DecodeBot: AI stands for Artificial Intelligence.")
        print("It enables machines to simulate human intelligence and solve problems.")

    # Chatbot questions
    elif user_input in ["what is a chatbot", "define chatbot"]:
        print("DecodeBot: A chatbot is a computer program designed to simulate conversations with users.")

    # Time feature
    elif user_input in ["time", "what time is it", "current time"]:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"DecodeBot: The current time is {current_time}.")

    # Exit commands
    elif user_input in ["bye", "exit", "quit"]:
        print("DecodeBot: Goodbye! Thank you for chatting with me. Have a great day! 👋")
        break

    # Empty input
    elif user_input == "":
        print("DecodeBot: Please type something so I can help you.")

    # Unknown commands
    else:
        print("DecodeBot: Sorry, I don't understand that yet.")
        print("Type 'help' to see the commands I support.")