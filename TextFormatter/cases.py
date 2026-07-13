# Main menu
def menu():
    print("\n"+ "*"*40)
    print("Text Formatter")
    print("*"*40 + "\n")
    print(f'''Cases options are:
          1. UPPERCASE
          2. lowercase
          3. Title Case
          4. Sentence case
          5. Swap case(lower to upper and vice-versa)
          6. camelCase
          7. PascalCase
          8. snake_case
          9. kebab-case
          \n''')
# All case function
# Upper case
def uppercase(text):
    return text.upper()
# Lower case
def lowercase(text):
    return text.lower()
# Title case
def titlecase(text):
    return text.title()
# Sentence case
def sentencecase(text):
    return text.capitalize()
# Swap case
def swapcase(text):
    return text.swapcase()
# Camel case
def camelcase(text):
    words = text.split()
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])
# Pascal case
def pascalcase(text):
    words = text.split()
    return "".join(word.capitalize() for word in words)