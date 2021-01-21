from collections import deque
lst = deque(x for x in input().split(" "))
print(f"{' '.join(x for x in reversed(lst))}")
