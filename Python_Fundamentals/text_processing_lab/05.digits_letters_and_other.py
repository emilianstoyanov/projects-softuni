text = input()

save_digit = []
save_letter = []
others = []

for letter in text:
    o = ord(letter)
    if o >= 48 and o <= 57:
        save_digit.append(chr(o))
    elif o >= 97 and o <= 122 or o >= 65 and o <= 90:
        save_letter.append(chr(o))
    else:
        others.append(chr(o))
        

print("".join(save_digit))
print("".join(save_letter))
print("".join(others))
