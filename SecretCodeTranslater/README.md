# 🔐Secret Code Translater
A Python-based **Secret Code Translater** that can encode and decode messages using a custom algorithm. To improve security, decoding requires a **secret key**(for now username is secret key), ensuring only authorised users can reveal the original message.
## 📌Features
- Encoding 
- Decoding
- Secret key verification
- Random characters added for extra security
- Supports multi-word messages.
## 🛠️Tehnologies Used
- Python 3.14.5
- **random** Module
- Git and Github
- VS Code
## 🔒Encoding Rules
- If the code contains atleast three character-
    - remove the first letter
    - append it at the end 
    - append three random characters at the starting and the end
- Else
    - Simply reverse the string
## 🔓Decoding Rules
**Before Decoding**
    - User must enter the secret key
    - If key not correct Access Denied
- If the code contains atleast three character
    - Remove 3 random characters from start and end
    - Remove the last letter
    - Append it to beginning
- Else 
    - Reverse the string
## 📂Project Structure
    |- secret_code.py
    |- README.md
    |- Encode.png
    |- Decode.png
    |- New.png
## 📚Concepts Used
- Variables
- Conditional Statements
- Strings
- String Slicing
- Loops
- User Input Handling
## 👩🏻‍💻Author 
    - Satyabhama Pani
    