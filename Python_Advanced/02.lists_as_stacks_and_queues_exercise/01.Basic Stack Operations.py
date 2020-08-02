numbers = [int(x) for x in input().split()]
to_push, to_pop, searched_numbers = numbers

elements = [int(x) for x in input().split()]

for _ in range(to_pop):  # [elements.pop() for _ in range(to_pop)]
    elements.pop()

if searched_numbers in elements:
    print("True")

else:
    if len(elements) == 0:
        print(0)
    else:
        print(min(elements))




