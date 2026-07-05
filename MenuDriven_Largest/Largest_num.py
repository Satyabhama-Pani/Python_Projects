#  welcome note
print("========Largest Number Checker========")
print('''
1. Press 1 to find largest of two numbers
2. Press 2 to find largest of three numbers
3. Press 3 to find largest of four numbers
''')
# ask user
num = int(input("choose any of the option: "))
choice = "yes"
while choice == "yes":
    if num < 5:
        match  num:
            #  largest between two numbers
            case 1:
                a = int(input("Enter a number: "))
                b = int(input("Enter a number: "))
                if a > b:
                    print(f"{a} is larger")
                else:
                    print(f"{b} is larger")
            # largest among three numbers
            case 2:
                a = int(input("Enter a number: "))
                b = int(input("Enter a number: "))
                c = int(input("Enter a number: "))
                if a > b:
                    if a > c:
                        print(f"{a} is largest")
                    else:
                        print(f"{c} is largest")
                else:
                    if b > c:
                        print(f"{b} is largest")
                    else:
                        print(f"{c} is largest")
            # largest among four numbers
            case 3:
                a = int(input("Enter a number: "))
                b = int(input("Enter a number: "))
                c = int(input("Enter a number: "))
                d = int(input("Enter a number: "))
                if a > b:
                    if a > c:
                        if a > d:
                            print(f"{a} is largest")
                        else:
                            print(f"{d} is largest")
                    else:
                        if c > d:
                            print(f"{c} is largest")
                        else:
                            print(f"{d} is largest")
                else:
                    if b > c:
                        if b > d:
                            print(f"{b} is largest")
                        else:
                            print(f"{d} is largest")
                    else:
                        if c > d:
                            print(f"{c} is largest")
                        else:
                            print(f"{d} is largest")
            # default case
            case _:
                print("No option available")
    choice = input("do you want to continue yes or no?").lower()
    if choice == "yes":
        num = num = int(input("choose any of the option: "))