text = input("Enter a word / sentence : ").lower()
a = e = i = o = u = 0
vowels = consonants = spaces = 0
for ch in text:
    if ch in 'aeiou':
        if ch == 'a':
            a += 1
        elif ch == 'e':
            e += 1
        elif ch == 'i':
            i += 1
        elif ch == 'o':
            o += 1
        elif ch == 'u':
            u += 1
        vowels += 1
    elif ch == ' ':
        spaces += 1
    elif ch.isalpha():
        consonants += 1
total = len(text)
print(f"Total character : {total}")
print(f"Number of vowels : {vowels}")
print(f'''a = {a}, e = {e}, i = {i}, o = {o}, u = {u}''')
print(f"Number of consonants : {consonants}")
print(f"Number of spaces : {spaces}")

        