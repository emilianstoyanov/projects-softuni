factor = int(input())
count = int(input())
current_number = 1
numbers = []

while len(numbers) < count:
    if current_number % factor == 0:
        numbers.append(current_number)
    current_number += 1

print(numbers)