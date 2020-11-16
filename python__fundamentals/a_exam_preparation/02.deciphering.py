encrypted = input()
search = input().split(" ")

save = []
for letter in encrypted:
    o = ord(letter)
    if 100 < o <= 125 or o == 35:
        m = o - 3
        ch = chr(m)
        save.append(ch)
    else:
        print("This is not the book you are looking for.")
        break

j = "".join(save)
print(j.replace(search[0], search[1]))