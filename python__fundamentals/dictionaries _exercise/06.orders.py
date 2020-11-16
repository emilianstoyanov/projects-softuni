quantities_dict = {}
prices_dict = {}
while True:
    input_line = input()

    if input_line == "buy":
        break

    (product, price_str, quantity_str) = input_line.split(" ")  # quantity = input_line[0], float(input_line[1], int(input_line[2])
    price = float(price_str) 
    quantity = int(quantity_str)

    prices_dict[product] = price

    if product not in quantities_dict:
        quantities_dict[product] = 0
    quantities_dict[product] += quantity

for (key, price) in prices_dict.items():
    total_sum = price * quantities_dict[key]
    print(f"{key} -> {total_sum:.2f}")
