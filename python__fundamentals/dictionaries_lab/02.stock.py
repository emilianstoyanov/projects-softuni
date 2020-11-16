def solve(products_quantity_str, products_str):
    values = products_quantity_str.split(" ")
    n = len(values)
    products_quantity_dict = {values[i]: int(values[i + 1]) for i in range(0, n, 2)}

    for product in products_str.split(" "):
        if product in products_quantity_dict:
            quantity = products_quantity_dict[product]
            print(f"We have {quantity} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")

solve(input(), input())
