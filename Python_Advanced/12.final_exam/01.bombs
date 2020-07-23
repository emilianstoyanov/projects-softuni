from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))

count_datura = 0
count_cherry = 0
count_smoke = 0

while bomb_effects and bomb_casings:
    current_bomb = bomb_effects[0]
    current_casing = bomb_casings[-1]
    total = current_bomb + current_casing

    if count_smoke >= 3 and count_cherry >= 3 and count_datura >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        if bomb_effects:
            print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
        else:
            print(f"Bomb Effects: empty")

        if bomb_casings:
            print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
        else:
            print(f"Bomb Casings: empty")


        print(f"Cherry Bombs: {count_cherry}")
        print(f"Datura Bombs: {count_datura}")
        print(f"Smoke Decoy Bombs: {count_smoke}")

        exit()

    if total == 40:
        count_datura += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif total == 60:
        count_cherry += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    elif total == 120:
        count_smoke += 1
        bomb_effects.popleft()
        bomb_casings.pop()

    else:
        bomb_casings[-1] -= 5

print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print(f"Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print(f"Bomb Casings: empty")


print(f"Cherry Bombs: {count_cherry}")
print(f"Datura Bombs: {count_datura}")
print(f"Smoke Decoy Bombs: {count_smoke}")
