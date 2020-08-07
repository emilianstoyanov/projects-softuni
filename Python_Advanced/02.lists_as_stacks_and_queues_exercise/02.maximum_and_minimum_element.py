from collections import deque

number = int(input())

stack = deque()

for _ in range(number):
    input_num = input().split()
    command = int(input_num[0])

    if command == 1:
        stack.append(int(input_num[1]))
    if stack:
        if command == 2:
            stack.pop()
        elif command == 3:
            print(max(stack))
        elif command == 4:
            print(min(stack))

print(', '.join([str(x) for x in reversed(stack)]))
