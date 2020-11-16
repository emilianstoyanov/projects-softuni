input_number = int(input())

numbers = []
filtered = []

for i in range(1, input_number + 1):
    new_number = int(input())
    numbers.append(new_number)

command = input()

for number in numbers:
    if command == "even":
        if number % 2 == 0:
            filtered.append(number)

    elif command == "odd":
        if number % 2 != 0:
            filtered.append(number)

    elif command == "negative":
        if number < 0:
            filtered.append(number)

    elif command == "positive":
        if number >= 0:
            filtered.append(number)

print(filtered)
