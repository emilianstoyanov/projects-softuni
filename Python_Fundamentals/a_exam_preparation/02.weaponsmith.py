text = input()

save_odd = []
save_even = []
receve = text.split("|")
while True:

    command = input().split()

    if command[0] == "Done":
        final = "".join(map(str, receve))
        print(f"You crafted {final}!")
        break

    if command[0] == "Move" and command[1] == "Left":
        position = int(command[2])
        if int(command[2]) == 0 or 0 > int(command[2]) or len(receve) < int(command[2]):
            continue
        else:
            idx1 = receve[position]
            idx2 = receve[position - 1]
            left1 = idx1
            left2 = idx2
            rem = receve[receve.index(left1)], receve[receve.index(left2)] = receve[receve.index(left2)], receve[
                receve.index(left1)]


    elif command[0] == "Move" and command[1] == "Right":
        position = int(command[2])
        if 0 > int(command[2]) or position >= int(len(receve) - 1):
            continue
        else:
            idx = receve[position]
            idx0 = receve[position + 1]

            left = idx
            left0 = idx0

            rem = receve[receve.index(left0)], receve[receve.index(left)] = receve[receve.index(left)], receve[
                receve.index(left0)]


    elif command[0] == "Check" and command[1] == "Even":
        count = 0
        for i in receve:
            if count % 2 == 0:
                save_even.append(i)
            count += 1
        print(" ".join(save_even))



    elif command[0] == "Check" and command[1] == "Odd":
        count = 1
        for i in receve:
            if count % 2 != 1:
                save_odd.append(i)
            count += 1
        print(" ".join(save_odd))
