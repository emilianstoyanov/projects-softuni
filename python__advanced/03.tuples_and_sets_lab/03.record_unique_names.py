count = int(input())
d = []

for i in range(count):
    name = input()

    if name not in d:
        d.append(name)

for j in d:
    print(j)
