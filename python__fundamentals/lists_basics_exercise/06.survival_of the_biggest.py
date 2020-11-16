numbers_list = map(lambda x: int(x), input().split(" "))
count = int(input())

save = []
current = 0

for number in numbers_list:
    save.append(number)


while count > current:
    current += 1
    removv = save.remove(min(save))

print(save)

