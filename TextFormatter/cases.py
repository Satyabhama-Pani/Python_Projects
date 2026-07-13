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
def uppercase(text):
    return text.upper()
def lowercase(text):
    return text.lower()
def titlecase(text):
    return text.title()
def sentencecase(text):
    return text.capitalize()
def swapcase(text):
    return text.swapcase()