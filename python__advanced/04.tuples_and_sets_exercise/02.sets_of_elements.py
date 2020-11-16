first, second = [int(x) for x in input().split()]

save_first = set()
save_second = set()

for i in range(first):
    n = int(input())
    save_first.add(n)

for i in range(second):
    n = int(input())
    save_second.add(n)

total = save_second & save_first

for j in total:
    print(j)
