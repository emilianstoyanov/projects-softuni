products = {}
command = input()
while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])
    if product not in products:
        products[product] = 0

    products[product] += quantity
    command = input()


print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")



# def read_until_command(end_command):
#     lines = []
#
#     while True:
#         command = input()
#         if command == "statistics":
#             break
#         lines.append(command)
#     return lines
#
#
# def print_quantities(quantities_dict):
#     print("Products in stock:")
#     for (product, quantity) in quantities_dict.items():
#         print(f"- {product}: {quantity}")
#
#     print(f"Total Products: {len(quantities_dict)}")
#     print(f"Total Quantity: {sum(quantities_dict.values())}")
#
#
# def solve(lines):
#     quantities_dict = {}
#     for line in lines:
#         (product, quantity_str) = line.split(": ")
#         if product not in quantities_dict:
#             quantities_dict[product] = 0
#
#         quantities_dict[product] += int(quantity_str)
#
#     print_quantities(quantities_dict)
#
#
# lines = read_until_command("statistics")
# # lines = ["bread: 4", "cheese: 2", "ham: 1", "bread: 1"]
# solve(lines)

























