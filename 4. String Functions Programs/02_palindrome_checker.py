text = input("Enter a word / sentence : ").lower()
rev = text[::-1]
if (rev == text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")