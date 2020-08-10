from collections import deque

numbers = deque(int(x) for x in input().split())

limit = int(input())

total = 0
count = 0

while numbers:
    last = numbers[-1]

    if total + last <= limit:
        total += last
        dd = numbers.pop()

    else:
        total = 0
        count += 1

if not numbers:
    count += 1
    print(count)
else:
    print(count)