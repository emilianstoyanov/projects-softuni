def solve(values):
    occurances = {}
    for value in values:
        if value in occurances:
            occurances[value] += 1
        else:
            occurances[value] = 1

    for numbers, count in occurances.items():
        print(f"{numbers} - {count} times")


values_strings = input().split(" ")
values = [float(x) for x in values_strings]
solve(values)
