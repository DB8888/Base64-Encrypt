import base64
message = input("Enter a word or phrase to translate...\n")
message = message[2:-1]
message = bytes(base64.b64decode(message))
print(str(message.decode()))
