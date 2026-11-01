#messages
messages = [
    "Hello", "Hi", 
    "How are you?", 
    "Good morning", 
    "Good night"
]
#def
def display_messages(messages_list):
    """Display a list of messages."""
    for message in messages_list:
        print(message)

display_messages(messages)