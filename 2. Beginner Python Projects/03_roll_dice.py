import random

choice = input("Do you want to roll the dice ? (y/n) : ").lower()
if (choice == 'y'):
        times = int(input("How many time do you want to roll the dice ? : "))
        results = []
        
        for i in range(times):
            dice = random.randint(1,6)
            results.append(dice)
        outcome = tuple(results)
        print(outcome)
elif(choice == 'n'):
        print("Exiting the program.....!")
else:
        print("Enter a valid response!")
