def average(numbers):
    return  sum(numbers) / len(numbers)

def solve(employees_strings, happiness_factor_stringst):
    employees = list(map(int, employees_strings.split(" ")))
    employees_count = len(employees)
    happiness_factor = int(happiness_factor_stringst)
    employees = list(map(
        lambda employee: employee * happiness_factor,
        employees))
    average_happiness = average(employees)
    happy_employess_count= len(list(filter(lambda employee: employee >= average_happiness, employees )))
    if happy_employess_count < employees_count // 2:
        print(f"Score: {happy_employess_count}/{employees_count}. Employees are not happy!")
    else:
        print(f"Score: {happy_employess_count}/{employees_count}. Employees are happy!")

solve(input(), input())
