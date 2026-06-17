# 🤖 DecodeBot — Rule-Based AI Chatbot
**Project 1 | Artificial Intelligence Track**
**Batch: 2026 | Powered by DecodeLabs**

---

## 📌 Project Overview

DecodeBot is a rule-based AI chatbot built using pure Python. It simulates basic human interaction through programmatic decision-making — no machine learning, no deep learning. Just clean control flow and logic.

This project forms the **foundation phase** of the AI Engineering track at DecodeLabs, proving the ability to build a deterministic, traceable intelligent interface from scratch.

---

## 🎯 Goal

Create a simple rule-based chatbot that responds to predefined user inputs using if-else logic, a continuous input loop, and a real-time clock feature.

---

## ⚙️ How It Works (IPO Model)

| Stage | What Happens |
|---|---|
| **Input** | User types a message |
| **Sanitization** | Input is cleaned using `.lower().strip()` so "Hello", "HELLO", and "hello" all match |
| **Process** | Cleaned input is matched against predefined intent groups using if-elif logic |
| **Output** | A matched response is printed, or a fallback message with a `help` tip is shown |

The chatbot runs in a continuous `while True` loop and only stops when the user types `bye`, `exit`, or `quit`.

---

## 🧠 Key Concepts Used

- **Control Flow** — `while True` loop with `if-elif-else` branching
- **Input Sanitization** — `.lower().strip()` normalizes all user input before matching
- **Intent Grouping** — Multiple phrases mapped to the same response using `in` lists
- **Real-Time Feature** — `datetime` module used to fetch and display the current time
- **Empty Input Handling** — Catches blank entries and prompts the user to type something
- **Fallback Response** — Unknown inputs get a helpful nudge to type `help`
- **Exit Strategy** — A clean `break` command ends the loop gracefully

---

## 🗂️ Project Structure

```
DecodeBot/
│
├── chatbot.py       # Main chatbot script
└── README.md        # Project documentation
```

---

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Open the project folder in **PyCharm**.
3. Run the script:

```bash
python chatbot.py
```

4. Start chatting! Type `help` to see available commands, or `exit` to quit.

---

## 💬 Sample Interaction

```
==================================================
🤖 Welcome to DecodeBot!
I am a Rule-Based AI Chatbot.
Type 'help' to see what I can do.
Type 'exit', 'bye', or 'quit' to end the chat.
==================================================

You: hello
DecodeBot: Hello! Nice to meet you. How can I help you today?

You: what is ai
DecodeBot: AI stands for Artificial Intelligence.
It enables machines to simulate human intelligence and solve problems.

You: what time is it
DecodeBot: The current time is 10:45 AM.

You: help
DecodeBot: Here are the things I can do:
• Greetings (hi, hello, hey)
• Ask me my name
• Respond to 'how are you'
• Explain what AI is
• Tell the current time
• Explain what a chatbot is
• Exit the conversation

You: bye
DecodeBot: Goodbye! Thank you for chatting with me. Have a great day! 👋
```

---

## 🗣️ Supported Intents

| Intent | Example Inputs |
|---|---|
| Greetings | `hi`, `hello`, `hey`, `good morning`, `good evening` |
| Bot's name | `what is your name`, `who are you`, `your name` |
| How are you | `how are you`, `how are you doing` |
| Help | `help` |
| What is AI | `what is ai`, `define ai`, `tell me about ai` |
| What is a chatbot | `what is a chatbot`, `define chatbot` |
| Current time | `time`, `what time is it`, `current time` |
| Exit | `bye`, `exit`, `quit` |
| Empty input | *(blank enter)* |
| Unknown | anything else |

---

## 📋 Specification Checklist

- [x] INPUT LOOP — Continuous `while` cycle
- [x] SANITIZATION — Handles case & whitespace
- [x] KNOWLEDGE BASE — 8 intents covered
- [x] FALLBACK — Default response for unknowns with `help` tip
- [x] EXIT STRATEGY — Clean `break` on `bye`, `exit`, or `quit`

---

## 🔑 Key Skills Demonstrated

- Python basics and syntax
- Control flow and decision-making logic
- Input sanitization and normalization
- Working with Python's `datetime` module
- Basic AI system architecture (IPO Model)
- Understanding of rule-based vs probabilistic AI systems

---

## 👨‍💻 Author

**Marvin Tettey | DecodeLabs AI Intern — Batch 2026**

---

*"Before you build systems that learn on their own, you must master the art of teaching a machine through explicit instructions."*
*— DecodeLabs*
