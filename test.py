from chatbot import chatbot

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    reply = chatbot(user)
    print("Bot:", reply)
