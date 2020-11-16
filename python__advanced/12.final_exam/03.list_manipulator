from collections import deque

def list_manipulator(numbers, add_remove, beginning_end, *args):
    numbers = deque(numbers)
    if add_remove == "add":
        if beginning_end == "end":
            for n in args:
                numbers.append(n)
        elif beginning_end == "beginning":
            for n in args[::-1]:
                numbers.appendleft(n)

    elif add_remove == "remove":
        if beginning_end == "end":
            if args:
                n = args[0]
                for i in range(n):
                    numbers.pop()
            else:
                numbers.pop()

        elif beginning_end == "beginning":
            if args:
                n = args[0]
                for i in range(n):
                    numbers.popleft()
            else:
                numbers.popleft()

    return [int(x) for x in numbers]


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
