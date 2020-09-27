legendaryItems = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
winner = ""
while winner == "":
    tokens = input().lower().split(" ")

    for index in range(0, len(tokens), 2):
        current_item = tokens[index + 1]
        quantity = int(tokens[index])

        if current_item in legendaryItems:
            legendaryItems[current_item] += quantity

            if legendaryItems[current_item] >= 250:
                legendaryItems[current_item] -= 250
                winner = current_item
                break
        else:
            if current_item not in junk:
                junk[current_item] = 0
            junk[current_item] += quantity

if winner == "shards":
    print("Shadowmourne obtained!")
elif winner == "fragments":
    print("Valanyr obtained!")
elif winner == "motes":
    print("Dragonwrath obtained!")

legendaryItems = dict(sorted(legendaryItems.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items()))

for (k, v) in legendaryItems.items():
    print(f"{k}: {v}")

for (k, v) in junk.items():
    print(f"{k}: {v}")


