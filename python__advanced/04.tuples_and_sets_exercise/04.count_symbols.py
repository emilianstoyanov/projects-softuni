text = input()

save = {}

for symbol in text:

    if symbol not in save:
        save[symbol] = 1
    else:
        save[symbol] += 1

for key, value in sorted(save.items(), key=lambda x: x[0]):
    print(f"{key}: {value} time/s")
