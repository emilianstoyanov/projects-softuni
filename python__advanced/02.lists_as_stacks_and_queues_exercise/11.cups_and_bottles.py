from collections import deque

wasted_litters_water = 0

cups_capacity = deque(int(x) for x in input().split())  # чаши за пълнене
bottles = deque(int(x) for x in input().split())  # бутилки с вода

while cups_capacity:

    cup = cups_capacity.popleft()
    bottle = bottles.pop()

    if bottle >= cup:
        wasted_litters_water += abs(bottle - cup)

    elif bottle < cup:
        while cup > 0:
            # wasted_litters_water += abs(bottle - cup)
            cup -= bottle

            if cup > 0:
                bottle = bottles.pop()

                if bottle > cup:
                    wasted_litters_water += abs(bottle - cup)
                    cup -= bottle

            else:
                cup -= bottle
    if len(bottles) == 0:
        break

if not cups_capacity:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")
    print(f"Wasted litters of water: {wasted_litters_water}")

else:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
    print(f"Wasted litters of water: {wasted_litters_water}")
