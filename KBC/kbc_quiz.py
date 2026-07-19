import os 

# Questions  dictionary
questions = {
    "In Hindi mythology, who is the elder brother Of lord Krishna": {
        "A": "Balarama",
        "B": "Lakshmana",
        "C": "Bharata",
        "D": "Dhritrashtra",
        "answer": "A"
    },
    "Which of the folloowing holy river flows directly through the ancient city of Varansi?": {
        "A": "Yamuna",
        "B": "Ganga",
        "C": "Bhramhaputra",
        "D": "Narmada",
        "answer": "B"
    },
    "Who was the founder of Maurya Empire?": {
        "A": "Bindusara",
        "B": "Samudragupta",
        "C": "Chandragupta Maurya",
        "D": "Ashoka The Great",
        "answer": "C"
    },
    "Which planet is widely known as Red Planet?": {
        "A": "Venus",
        "B": "Mars",
        "C": "Mercury",
        "D": "Jupiter",
        "answer": "B"
    },
    "Which city is known as Marble city?": {
        "A": "Agra",
        "B": "Jaiur",
        "C": "Udaipur",
        "D": "Jabalpur",
        "answer": "D"
    }
}

# player names and prizes
player_names =[]
player_prizes = []

#  prize money list
prizes = [1000,2000,5000,10000,50000]

# Welcome note
print("*" * 50)
print("\t\tWelcome to QuizMaster\U0001F3C6")
print("*" * 50)

# main logic starts
n = int(input("Enter number of player: "))
for i in range(n):
    name = input(f"Enter player{i+1} name: ")
    prize = 0
    counter= 0
    for question,data in questions.items(): 
        # display question and option
        print(f"\nQuestion {counter + 1}: {question}")
        for option in ['A','B','C','D']:
            print(f"{option}. {data[option]}")
        #  take answer and match 
        user_ans = input("Enter your answer(A/B/C/D) or Q to quit: ").upper()
        if user_ans == "Q":
            print("You Quit the game...")
            print(f"You can take home money: ₹{prize}")
            break
        if user_ans.lower() == data["answer"].lower():
            print("Correct!\u2705")
            prize = prizes[counter]
            print(f"Current Prize: ₹{prize}\U0001F4B0")
        else:
            print("Wrong","GAME OVER",sep="\n")
            print("Correct answer", data["answer"])
            break
        counter += 1
        print(f"Questions answered: {counter}/{len(questions)}\u2B50")
    player_names.append(name)
    player_prizes.append(prize)
    if i < n-1:
        input("Press Enter to start to next player's turn...")
        os.system("cls")

# store player with highest money
highest = max(player_prizes)
winner_index = player_prizes.index(highest)

# leaderboard
print("\n" + "*"*40)
print(f"{"Leaderboard":^40}")
print("*"*40)

for i in range(len(player_names)):
    if i == winner_index:
        # bonus for player with highest prize
        if n > 1:
            player_prizes[i] += 10000
        print(f"{player_names[i]}:  ₹{player_prizes[i]} \U0001F3C6")
    else:
        print(f"{player_names[i]}: ₹{player_prizes[i]}")
    print()

# display highest scorer
if n > 1:
    print("="*40)
    print(f'''Winner: {player_names[winner_index]}
    \U0001F31FBonus: ₹10000
    Final Prize: {player_prizes[winner_index]}
    ''')
