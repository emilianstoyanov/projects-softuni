def func_executor(*args):
    result = []
    for el in args:
        function = el[0]
        arguments = el[1]
        result.append(function(*arguments))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2
