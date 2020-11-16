text = input()

save = []

for letter in text:
    o = ord(letter) + 3
    ch = chr(o)
    save.append(ch)

print("".join(save))
