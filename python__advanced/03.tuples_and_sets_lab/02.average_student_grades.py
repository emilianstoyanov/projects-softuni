count = int(input())

save = {}

for i in range(count):
    text = input().split(" ")
    name = text[0]
    num = float(text[1])

    if name not in save.keys():
        save[name] = [num]
    else:
        save[name].append(num)

for key, value in save.items():
    print(value)
    new = ' '.join(f'{x:.2f}' for x in value)
    print(f"{key} -> {new} (avg: {sum(value) / len(value):.2f})")

