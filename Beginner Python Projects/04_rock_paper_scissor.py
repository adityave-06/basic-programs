import random

choices = ["rock", "paper", "scissors"]
w_count = 0
l_count = 0
t_count = 0

while True:
    user = input("Enter your choice (rock/paper/scissors): ").lower()
    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print(f"You chose : {user}")
    print(f"System chose : {computer}")

    if user == computer:
        print("It's a tie..!")
        t_count += 1
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("You win..!")
        w_count += 1
    else:
        print("Computer wins..!")
        l_count += 1

    print(f"Tie count : {t_count}")
    print(f"Win count : {w_count}")
    print(f"Loss count : {l_count}")

    again = input("Do you want to play again (y/n): ").lower()
    if again == 'n':
        print("Thank you for playing...")
        break
