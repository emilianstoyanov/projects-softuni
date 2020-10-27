n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    summed = sum([ord(x) for x in name]) // i

    if summed % 2 == 0:
        even_set.add(summed)
    else:
        odd_set.add(summed)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    union_values = odd_set.union(even_set)
    print(', '.join([str(x) for x in union_values]))

elif odd_sum > even_sum: 
    different_values = odd_set.difference(even_set)
    print(', '.join([str(x) for x in different_values]))
else:
    symmetric_values = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in symmetric_values]))
