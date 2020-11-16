people = []
vip = []

while True:
    text = input()
    if text == "PARTY":
        break
    digit = text[0]
    if digit.isdigit() and len(text) == 8:
        vip.append(text)
    else:
        if len(text) == 8:
            people.append(text)
count = 0
while True:
    stop = input()
    if stop == "END":
        break
    dig = stop[0]
    if dig.isdigit():
        if stop not in vip:
            count += 1
        else:
            vip.remove(stop)
    else:
        if stop not in people:
            count += 1
        else:
            people.remove(stop)

print(f"{len(people) + len(vip)}")
for h in sorted(vip, key=lambda x: x[0]):
    print(f"{h}")

for i in sorted(people, key=lambda k: k[0]):
    print(f"{i}")
