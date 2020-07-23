from collections import deque

men = deque(int(x) for x in input().split(" "))
women = deque(int(x) for x in input().split(" "))

matches = 0
while men and women:
    final_men = men.pop()
    first_women = women.popleft()

    if final_men <= 0 and first_women <= 0:
        continue

    if final_men > 0 and first_women <= 0:
        men.append(final_men)
        continue

    if final_men <= 0 and first_women > 0:
        women.appendleft(first_women)
        continue

    if final_men % 25 == 0 and first_women % 25 == 0:
        if men:
            men.pop()
        if women:
            women.popleft()
        continue

    if final_men % 25 == 0 and first_women % 25 != 0:
        if men:
            men.pop()
        women.appendleft(first_women)
        continue

    if first_women % 25 == 0 and final_men % 25 != 0:
        if women:
            women.popleft()
        men.append(final_men)
        continue

    if first_women == final_men:
        matches += 1
        continue

    if final_men != first_women:
        extraction = final_men - 2
        men.append(extraction)
        continue

print(f"Matches: {matches}")

if men:
    print(f"Males left: {', '.join(str(x) for x in reversed(men))}")
elif not men:
    print(f"Males left: none")

if women:
    print(f"Females left: {', '.join(str(x) for x in women)}")
elif not women:
    print(f"Females left: none")
