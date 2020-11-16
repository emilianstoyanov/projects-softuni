from collections import deque
all_food = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))


while orders:
    customer = orders.popleft()

    if all_food >= customer:
        all_food -= customer

    else:
        orders.appendleft(customer)
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break

if not orders:
    print("Orders complete")
