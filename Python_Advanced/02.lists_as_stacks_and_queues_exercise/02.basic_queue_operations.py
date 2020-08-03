from collections import deque

numbers = [int(x) for x in input().split()]  # обръщаме от текст в числа
to_push, to_pop, searched_numbers = numbers

el_num = [int(x) for x in input().split()]
elements = deque()

for num in el_num:
    elements.append(num)

for _ in range(to_pop):  # [elements.pop() for _ in range(to_pop)]
    elements.popleft()

if searched_numbers in elements:
    print("True")

else:
    if len(elements) == 0:
        print(0)
    else:
        print(min(elements))
