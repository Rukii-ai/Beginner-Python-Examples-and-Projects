short_messages = ["Hello, world!",
            "Enjoy the simple things.",
            "Keep going.",
            "Today is a good day.",
            "Be kind."]
sent_messages = []

def sending_messages(messages_not_sent, messages_sent):
    """Receives a list of messages and prints them individually"""
    
    while messages_not_sent:
        message = messages_not_sent.pop()
        print(f"Sending message: {message}")
        messages_sent.append(message)
    
    print("\nThe following messages were sent: ")
    print(messages_sent)


sending_messages(short_messages[:], sent_messages)
print(short_messages)
print(sent_messages)


"""
Blue colours --> Variables

Yellow colours --> Functions
"""