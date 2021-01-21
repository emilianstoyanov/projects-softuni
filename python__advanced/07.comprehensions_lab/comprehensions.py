x = [1, 2, 3, 4, 5, 6]
filtred = [num for num in x if num % 2 == 0]
print(filtred)  # [2, 4, 6]


y = 5
print('Even' if y % 2 == 0 else 'Odd')
# ако е четно, принтирай 'Even', иначе принтирай 'Odd'


n = 10
m = 4
step = +1 if n < m else -1
result = [x for x in range(n, m, step)]
print(result)
# ako n < m [4, 5, 6, 7, 8, 9]
# ako n > m [10, 9, 8, 7, 6, 5]


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x % 3 for x in n])
print({x % 3 for x in n}) # запазва уникалните стойности
# [1, 2, 0, 1, 2, 0, 1, 2, 0, 1]
# {0, 1, 2}



