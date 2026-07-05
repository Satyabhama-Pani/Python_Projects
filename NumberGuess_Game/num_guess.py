# The Perfect Guess
import random as r
import os 
n = r.randint(7,777)
players = {}

# Welcome note
print("=" * 60)
print("\t\U0001F44B Welcome to the \U0001F50E PERFECT GUESS GAME \U0001F947")
print("=" * 60)

# enter no of players
noPlayer= int(input("\nEnter how many players you are:"))
for i in range(1,noPlayer+1):
    name = input(f"Enter \U0001F464 player {i} Name: ")
    you = -1
    guess = 0
    print(f"\n{name}, you have to enter number ranges from 1 to 1000")
    while(you != n):
        guess+=1
        you = int(input("Guess a number\U0001F50E: "))
        if(you < n):
            print("Higher number please")
        elif(you > n):
            print("Lower number please")
    print(f"{name}, \u2728 you guess the exact number correctly in {guess} attempts")
    players[name] = guess
    if(i != noPlayer):
        input("Press enter key for next player...")
        os.system("cls")
    else:
        input("Press enter key to see scoreboard...")
        os.system("cls")

# Player with minimum attempts win the game 
minAttempts = 999
winner = []
for player in players:
    if(players[player] < minAttempts):
        minAttempts = players[player]
        winner = [player]
    elif(players[player] == minAttempts):
        winner.append(player)

# Scoreboard
print("\n\t\t\U0001F3AF Scoreboard \U0001F3AF")
print("=" * 55)
print(f"{"Players": <22}\t{"Attempts"}\t\t{"Winners"}")
print("=" * 55)

for name, attempts in players.items():
    if name in winner:
        print(f"\U0001F947 {name:<20}\t{attempts}\t\t\t\U0001F3C6 ")
    else:
        print(f"\U0001F464 {name:<20}\t{attempts}")