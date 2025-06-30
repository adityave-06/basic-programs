text = input("Enter a string : ")
lower = upper = 0
for ch in text:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
        
print(f"Upper Case letter : {upper}")
print(f"Lower Case letter : {lower}")