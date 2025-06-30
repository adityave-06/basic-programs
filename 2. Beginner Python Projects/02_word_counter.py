para = input("Enter your paragraph / sentence : ").lower()
word_counter = para.split()
print(f"Total number of words are : {len(word_counter)}")
print("Do you want to know the frequency of a particular word? (Y/N) : ")
choice = input()
if choice.lower() == "y":
    word = input("Enter the word to check its frequency : ").lower()
    freq = word_counter.count(word)
    print(f"The frequency of '{word}' is : {freq}")
elif(choice.lower() == "n"):
    print("Exiting the program.......")
else:
    print("Invalid choice.")
print("The total characters in you paragraph : ")
print(len(para.replace(" ","")))
# How are you Aditya Verma
