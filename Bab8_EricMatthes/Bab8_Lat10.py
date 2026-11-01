#sending messages
messages = [
    "Hello", "Hi", 
    "How are you?", 
    "Good morning", 
    "Good night"
]
sent_messages = []

def send_messages(messages_list, sent_messages_list):
    """Send messages and move them to the sent list."""
    while messages_list:
        current_message = messages_list.pop()
        print(f"Sending message: {current_message}")
        sent_messages_list.append(current_message)

send_messages(messages[:], sent_messages)
print("\nOriginal messages:")
print(messages)
print("\nSent messages:")
print(sent_messages)