def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == "even":
        return [int(x) for x in numbers if x % 2 == 0]
    else:
        return [int(x) for x in numbers if x % 2 == 1]
