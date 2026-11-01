#Archived messages
#call function send_messages() from Bab8_Lat10.py and display the sent messages


from Bab8_EricMatthes.Bab8_Lat10 import send_messages


messages = [
    "Hello", "Hi", 
    "How are you?", 
    "Good morning", 
    "Good night"
]
sent_messages = []

send_messages(messages, sent_messages)
print("\nOriginal messages:")
print(messages)
print("\nSent messages:")
print(sent_messages)