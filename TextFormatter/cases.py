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
# Snake case
def snakecase(text):
    words = text.split()
    return "_".join(word.lower() for word in words)
# Kebab case
def kebabcase(text):
    words = text.split()
    return "-".join(word.lower() for word in words)
# get input
def get_input():
    while True:
        try:
            t = input("Enter the text: ").strip()
            if t.isdecimal():
                raise ValueError("Input cannot contain only numbers")
            if not t:
                raise ValueError("Empty input")
            return t
        except ValueError as e:
            print(f"Error: {e}")