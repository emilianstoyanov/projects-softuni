text = input()
save = []

pairs = {
    "{": "}",
    "[": "]",
    "(": ")"}

valid = True

for el in text:
    if el in "({[":
        save.append(el)
    elif el in ")}]":
        if save:
            current = save[-1]
            if pairs[current] == el:
                save.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break
if valid:
    print("YES")
else:
    print("NO")
