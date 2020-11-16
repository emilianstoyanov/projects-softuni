line = input().split("|")
coins = 100
energy = 100

completed = True

for command in line:
    tokens = command.split("-")
    if tokens[0] == "rest":
        added_energy = int(tokens[1])
        if energy + added_energy <= 100:
            energy += added_energy
            print(f"You gained {added_energy} energy.")
        else:
            print(f"You gained 0 energy.")
        print(f"Current energy: {energy}.")

    elif tokens[0] == "order":
        new_coins = int(tokens[1])
        if energy - 30 >= 0:
            coins += new_coins
            energy -= 30
            print(f"You earned {new_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        ingredient = tokens[0]
        cost = int(tokens[1])

        if coins <= 0:
            print(f"Closed! Cannot afford {ingredient}.")
            completed = False
            break

        if coins - cost > 0:
            coins -= cost
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            completed = False
            break

if completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")





