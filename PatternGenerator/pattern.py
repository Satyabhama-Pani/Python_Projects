# welcome note
def menu():
    print("\n")
    print("*"*40)
    print(f"{"\u2728 Pattern Generator\u2728":^40}")
    print("*"*40)
    print("\n")
    print(f"""Options are: 
    1. Square Pattern
    2. left Triangle Pattern
    3. Right Triangle Pattern
    4. Inverted Triangle
    5. Pyramid Pattern
    6. Inverted Pyramid Pattern
    7. Diamond Pattern
    8. Hollow Square
    \n""")
# validate input 
def get_input():
    while True:
        char = input("Enter a single character: ")
        if len(char)== 1:
            break
        print("Please enter only One character")
    while True:
        size = int(input("Enter size: "))
        if size > 0:
            break
        print("Size must be greater than 0")
    return char, size
# patterns 
def square(n,c):
    for i in range(n):
        for j in range(n):
            print(c,end=" ")
        print()

def left_triangle(n,c):
    for i in range(1,n+1):
        for j in range(i):
            print(c,end=" ")
        print()

def right_triangle(n,c):
    for i in range(1,n+1): 
        print("  "*(n-i),end="")
        for j in range(i):
            print(c,end=" ")
        print()

def inverted_triangle(n,c):
    for i in range(n, 0, -1):
        for j in range(i):
            print(c, end=" ")
        print()

def pyramid(n,c):
    for i in range(1, n+1):
        print(" "*(n-i), end="")
        print(c*(2*i-1))

def inverted_pyramid(n,c):
    for i in range(n, 0, -1):
        print(" "*(n-i), end="")
        print(c*(2*i-1))

def diamond(n,c):
    # upper part
    for i in range(1, n+1):
        print(" "*(n-i), end="")
        print(c*(2*i-1))
    # lower part
    for i in range(n-1, 0, -1):
        print(" "*(n-i), end="")
        print(c*(2*i-1))

def hollow_square(n,c):
    for i in range(n):
        for j in range(n):
            if i==0 or i == n-1 or j == 0 or j== n-1:
                print(c,end=" ")
            else:
                print(" ", end=" ")
        print()

# dictionary mapping
patterns = {
    1: square,
    2: left_triangle,
    3: right_triangle,
    4: inverted_pyramid,
    5: pyramid,
    6: inverted_pyramid,
    7: diamond,
    8: hollow_square
}

# main program
choice = "yes"
while choice == "yes":
    menu()
    opt = int(input("Enter your choice: "))
    if opt == 0:
        print("Thankyou for using \u2728Pattern Generator\u2728")
        break
    if opt not in patterns:
        print("Invalid choice")
        continue
    char,size = get_input()
    print()
    patterns[opt](size,char)
    print()
    choice = input("Do you want to continue? ").lower()
