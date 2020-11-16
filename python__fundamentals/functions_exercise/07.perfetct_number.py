number = int(input())


def is_perfect(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors) == number


if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
