
sides = {}
while True:
    input_lines = input()

    if input_lines == "Lumpawaroo":
        break

    tokens = input_lines.split(" | ")


    if len(tokens) == 2:
        (side, user) = tokens
        is_contain  = False
        for (key, value) in sides.items():
            if user in value:
                is_contain = True
                break

        if not is_contain:
            if side not in sides:
                sides[side] = []
            sides[side].append(user)


    else:
        tokens = input_lines.split(" -> ")
        (user, side) = tokens

        for (key, value) in sides.items():
            if user in value:
                sides[key].remove(user)
                break

        if side not in sides:
            sides[side] = []
        sides[side].append(user)
        print(f"{user} joins the {side} side!")


sorted_force_side = dict(sorted(sides.items(), key=lambda z: (-len(z[1]), z[0])))

for (key,value) in sorted_force_side.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        [print(f"! {user}") for user in sorted(value)]


