numbers = list(map(int, input().split(", ")))  # 2, 3, 4, 5, 6, 10, 4

indices_for = []     # [0, 2, 4, 5, 6]

for i in range(len(numbers)):
    number = numbers[i]
    if number % 2 == 0:
        indices_for.append(i)
print(indices_for)
