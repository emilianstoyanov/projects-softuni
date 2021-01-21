import math
from collections import deque

lst = deque(x for x in input().split(" "))
first_for = 0
moment_lst = deque()
total = 0
chars = ['+', '-', '*', '/']
total_moment = 0

for symbol in lst:
    if symbol not in chars:
        moment_lst.append(int(symbol))
    else:
        if symbol == "-":
            if first_for == 0:
                first_num = moment_lst.popleft()
                for n in moment_lst:
                    first_num -= n
                total_moment = first_num
                total = total_moment
                moment_lst.clear()
                first_for += 1
                continue
            else:
                for k in moment_lst:
                    total_moment -= k
                total = total_moment
                moment_lst.clear()

        elif symbol == "*":
            if first_for == 0:
                first_num = moment_lst.popleft()
                for n in moment_lst:
                    first_num *= n
                total_moment = first_num
                total = total_moment
                moment_lst.clear()
                first_for += 1
                continue
            else:
                for p in moment_lst:
                    total_moment *= p
                total = total_moment
                moment_lst.clear()

        elif symbol == "/":
            if first_for == 0:
                first_num = moment_lst.popleft()
                for n in moment_lst:
                    first_num /= n
                total_moment = math.floor(first_num)
                total = total_moment
                moment_lst.clear()
                first_for += 1
                continue
            else:
                for d in moment_lst:
                    total_moment /= d
                total = math.floor(total_moment)
                total_moment = total
                moment_lst.clear()

        elif symbol == "+":
            if first_for == 0:
                first_num = moment_lst.popleft()
                for n in moment_lst:
                    first_num += n
                total_moment = first_num
                total = total_moment
                moment_lst.clear()
                first_for += 1
                continue
            else:
                for d in moment_lst:
                    total_moment += d
                total = total_moment
                total_moment = total
                moment_lst.clear()

print(total)
