import math

biscuits = int(input())
count_workers = int(input())
amount_biscuits = int(input())

total = 0
for i in range(1, 31):

    if i % 3 == 0:
        total += (count_workers * biscuits) * 0.75

    else:
        total += count_workers * biscuits

print(f"You have produced {math.floor(total)} biscuits for the past month.")

difference = int(total - amount_biscuits)
if (int(total)) > amount_biscuits:
    print(f"You produce {((difference / amount_biscuits) * 100):.2f} percent more biscuits.")
else:
    print(f"You produce {(abs(difference / amount_biscuits) * 100):.2f} percent less biscuits.")
