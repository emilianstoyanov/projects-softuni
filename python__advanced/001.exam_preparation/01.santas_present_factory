from collections import deque

boxes_materials = deque(int(x) for x in input().split(" "))
magic_values = deque(int(x) for x in input().split(" "))

gifts = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

count_gifts = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while boxes_materials and magic_values:

    right_material = boxes_materials.pop()
    left_magic = magic_values.popleft()

    if right_material == 0 and left_magic > 0:
        magic_values.appendleft(left_magic)
        continue
    if right_material > 0 and left_magic == 0:
        boxes_materials.append(right_material)
        continue
    if right_material == 0 and left_magic == 0:
        continue

    multiplication = left_magic * right_material

    if multiplication in gifts:
        count_gifts[gifts[multiplication]] += 1

    elif multiplication < 0:  # ако е отрицателна сумираме и връщаме към материалите
        collection = right_material + left_magic
        boxes_materials.append(collection)

    elif multiplication > 0: 
        s = right_material + 15
        boxes_materials.append(s)

if count_gifts["Doll"] > 0 and count_gifts["Wooden train"] > 0 or count_gifts["Teddy bear"] > 0 and count_gifts[
    "Bicycle"] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes_materials))}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for key, value in sorted(count_gifts.items()):
    if value:
        print(f"{key}: {value}")
