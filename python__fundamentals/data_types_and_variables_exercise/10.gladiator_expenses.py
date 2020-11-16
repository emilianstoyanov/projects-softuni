lost_fights_count = int(input())

helmet_price = float(input())  # каска
sword_price = float(input())  # меч
shield_price = float(input())  # щит
armor_price = float(input())  # броня

helmet = 0
sword = 0
shieled = 0
armor = 0

for i in range(1, lost_fights_count + 1):

    if i % 2 == 0:
        helmet += 1

    if i % 3 == 0:
        sword += 1

    if i % 2 == 0 and i % 3 == 0:
        shieled += 1
        if shieled % 2 == 0:
            armor += 1

total = helmet * helmet_price + sword * sword_price + shieled * shield_price + armor * armor_price
print(f"Gladiator expenses: {total:.2f} aureus")
