number = input()


def get_sums(number):
    return [sum(list(map(int, filter(lambda x: int(x) % 2 == 0, number)))),
            sum([int(x) for x in number if int(x) % 2 == 1])]


result = get_sums(number)
print(f"Odd sum = {result[1]}, Even sum = {result[0]}")