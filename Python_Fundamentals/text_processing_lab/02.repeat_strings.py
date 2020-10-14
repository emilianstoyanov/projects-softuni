text = input().split(" ")

save = []

for word in text:
    l = len(word)
    save.append(word * l)

print("".join(save))
