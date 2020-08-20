vowels = {'a', 'o', 'u', 'e', 'i'}
text = input()
filter = [letter for letter in text if letter.lower() not in vowels]
print(''.join(filter))
