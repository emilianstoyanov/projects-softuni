shops = input().split(" ")
count = int(input())

for i in range(1, count + 1):

    commands = input().split(" ")

    if commands[0] == "Include":
        new_shop = commands[1]
        a = shops.append(new_shop)


    elif commands[0] == "Visit" and commands[1] == "last":
        idx = int(commands[2])
        if idx >= 0 and idx <= len(shops):
            c = shops[:-idx]
            shops = c
        else:
            continue

    elif commands[0] == "Visit" and commands[1] == "first":
        idx1 = int(commands[2])
        if idx1 >= 0 and idx1 <= len(shops):
            p = shops[idx1:]
            shops = p
        else:
            continue

    elif commands[0] == "Prefer":
        first = int(commands[1])
        second = int(commands[2])
        if first >= 0 and second >= 0 and first <= len(shops) and second <= len(shops):
            idxx = shops[first]
            idx2 = shops[second]
            s = shops[first], shops[second] = shops[second], shops[first] 
            # rem = shops[shops.index(idx2)], shops[shops.index(idxx)] = shops[shops.index(idxx)], shops[shops.index(idx2)]

        else:
            continue

    elif commands[0] == "Place":
        name_shop = commands[1]
        shop_index = int(commands[2])
        if shop_index >= 0 and shop_index + 1 <= len(shops):
            a = shops.insert(shop_index + 1, commands[1])

        else:
            continue
print("Shops left:")
print(" ".join(shops))
