command = input()

numbers = [int(x) for x in input().split()]

if command == "Odd":
    print(sum([x for x in numbers if x % 2 == 1]) * len(numbers))
else:
    print(sum([x for x in numbers if x % 2 == 0]) * len(numbers))
