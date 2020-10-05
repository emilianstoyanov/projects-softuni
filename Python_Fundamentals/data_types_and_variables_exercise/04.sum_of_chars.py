number = int(input())

total = 0
for i in range(1, number + 1):

    alphabet = input()
    convertion = ord(alphabet)
    total += convertion

print(f"The sum equals: {total}")
