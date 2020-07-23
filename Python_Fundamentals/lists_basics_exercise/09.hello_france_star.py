text = input().split("|")
budget = int(input())

total_price = 0
total = 0
for command in text:
    collection = command.split("->")

    if collection[0] == "Clothes":
        price = float(collection[1])
        if price <= 50:
            if budget >= price:
                budget -= price
                convert = price + (price * 0.40)
                total_price += convert
                total += price
                print(f"{convert:.2f}", end=" ")

    elif collection[0] == "Shoes":
        price = float(collection[1])
        if price <= 35:
            if budget >= price:
                budget -= price
                convert = price + (price * 0.40)
                total_price += convert
                total += price
                print(f"{convert:.2f}", end=" ")


    elif collection[0] == "Accessories":
        price = float(collection[1])
        if price <= 25.50:
            if budget >= price:
                budget -= price
                convert = price + (price * 0.40)
                total_price += convert
                total += price
                print(f"{convert:.2f}", end=" ")


print(f"\nProfit: {total_price - total:.2f}")

if budget + total_price >= 150:
    print("Hello, France!")
else:
    print("Time to go.")