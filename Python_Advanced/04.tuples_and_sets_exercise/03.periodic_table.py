num = int(input())

save = set()

for i in range(num):
    chemical = input().split()

    for element in chemical:
        save.add(element)

for j in save:
    print(j)
