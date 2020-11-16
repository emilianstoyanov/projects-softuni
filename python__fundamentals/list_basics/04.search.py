number = int(input())
word = input()

save = []

for i in range(number):
    current_string = input()
    save.append(current_string)
print(save)

for i in range(len(save) -1, -1, -1):
    element = save[i]
    if word not in element:
        save.remove(element)
print(save)
