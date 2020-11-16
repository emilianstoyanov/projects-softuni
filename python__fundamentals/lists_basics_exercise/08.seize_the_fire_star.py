text = input().split("#")
water = int(input())

effort = 0
total_fire = 0
count = 1
for command in text:

    if count == 1:
        print("Cells:")
        count += 1
    convert = command.split(" = ")
    if convert[0] == "High":
        amount = int(convert[1])
        if 81 <= amount <= 125:
            if water - amount >= 0:
                water -= amount
                effort += amount * 0.25
                total_fire += amount
                print(f" - {amount}")
            else:
                break

    elif convert[0] == "Medium":
        amount = int(convert[1])
        if 51 <= amount <= 80:
            if water - amount >= 0:
                water -= amount
                effort += amount * 0.25
                total_fire += amount
                print(f" - {amount}")
            else:
                break


    elif convert[0] == "Low":
        amount = int(convert[1])
        if 1 <= amount <= 50:
            if water - amount >= 0:
                water -= amount
                effort += amount * 0.25
                total_fire += amount
                print(f" - {amount}")
            else:
                break


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
