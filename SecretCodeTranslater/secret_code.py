#  generate  random characters
import random as r
chars = "abcdefghijklmnopqrstuvwxyz"

# original message
username = input("Enter your username: ")
message = input("Enter your message: ")
temp = message.split()

# encoded logic
encoded = []
for word in temp:
    if len(word) >= 3:
        # remove first and add to last
        word = word[1:] + word[0]  
        # add random character
        start = "".join(r.choice(chars) for _ in range(3))
        end = "".join(r.choice(chars) for _ in range(3))
        word = start + word + end
        encoded.append(word)
    else:
        word = word[::-1]
        encoded.append(word)

# decoded message 
encoded_msg = " ".join(encoded)
print()
print(f"Encoded message: {encoded_msg}")

# validate authority
user_key = input("\nEnter the key to decode: ")
key = username ## who can decode message 

# decoded logic
decoded = []
for word in encoded:
    if user_key == key:
        if len(word) >= 3:
            # remove random charaters
            word = word[3:-3]
            # remove last and add to first
            word = word[-1] + word[:-1]
            decoded.append(word)
        else:
            word = word[::-1]
            decoded.append(word)
decoded_msg = " ".join(decoded)
print(f"Decoded message: {decoded_msg}")