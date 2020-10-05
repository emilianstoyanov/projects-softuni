number = int(input())

capacity = 255
total = 0
total_sum = 0

for i in range(1, number + 1):

    liters_of_water = int(input())
    total += liters_of_water

    if capacity >= total:
        total_sum += liters_of_water
        continue

    else:
        print("Insufficient capacity!")
        total -= liters_of_water
        continue

print(f"{total_sum}")
