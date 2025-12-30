short_messages = ["Hello, world!",
            "Enjoy the simple things.",
            "Keep going.",
            "Today is a good day.",
            "Be kind."]

def show_messages(messages):
    """Receives a list of messages and prints them individually"""
    for message in messages:
        print(f"{message}")

show_messages(short_messages)