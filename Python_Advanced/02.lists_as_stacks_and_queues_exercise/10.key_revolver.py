from collections import deque

save = []
count = 0
ss = 0
price_bullet = int(input())  # цена на един куршум
size_gun_barrel = int(input())  # размер на цевта на пистолета
all_bullet = deque(int(x) for x in input().split(" "))  # всички куршуми
all_locks = deque(int(x) for x in input().split(" "))  # всички ключалки
value_the_intelligence = int(input())  # стойността на интелигентността

while True:

    bullet = all_bullet.pop()
    locks = all_locks.popleft()
    save.append(bullet)

    if bullet > locks:
        all_locks.appendleft(locks)
        print("Ping!")
        count += 1
        ss += 1
    elif bullet <= locks:
        print("Bang!")
        count += 1
        ss += 1


    if len(all_bullet) == 0 and len(all_locks) > 0:
        print(f"Couldn't get through. Locks left: {len(all_locks)}")
        exit()

    if size_gun_barrel == count:
        print("Reloading!")
        save.clear()
        count = 0

    if len(all_locks) == 0:
        s = price_bullet * ss
        print(f"{len(all_bullet)} bullets left. Earned ${value_the_intelligence - s}")
        exit()
