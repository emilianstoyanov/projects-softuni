save = []
while True:
    text = input()
    if text == "END":
        break

    spl = text.split(", ")
    command = spl[0]
    numbers = spl[1]

    if command == "IN":
        if numbers not in save:
            save.append(numbers)

    elif command == "OUT":
        if numbers in save:
            save.remove(numbers)

if save:
    for num in save:
        print(num)
else:
    print("Parking Lot is Empty")
