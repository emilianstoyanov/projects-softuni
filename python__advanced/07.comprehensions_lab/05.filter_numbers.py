def is_valid(number):
    min_number = 2
    max_number = 10

    for i in range(min_number, max_number + 1):
        if number % i == 0:
            return True
    return False


n = int(input())
m = int(input())

result = [x for x in range(n, m + 1) if is_valid(x)]
print(result)
