def replies(user_input):
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand"
    
while("bye"):
    user_input = input("You: ")
    user_input = user_input.lower().strip()
    reply = replies(user_input)
    print("Bot: ", reply)
    if user_input == "bye":
        break
