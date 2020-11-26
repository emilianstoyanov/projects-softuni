def print_rhombus(n: int):  # global namespace
    GROWING: int = 1  # local namespace
    SHRINKING: int = -1

    # fn-in-fn: closure
    def print_line(i: int, direction: int):  # local namespace
        if i == 0:
            return
        line = ' ' * (n - i) + '* ' * i
        print(line.rstrip())
        if i == n:
            direction = SHRINKING
        print_line(i + direction, direction)  # recursion

    print_line(1, GROWING)


print_rhombus(int(input()))
