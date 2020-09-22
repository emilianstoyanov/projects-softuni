
text = input()
save = []
spl = text.split(" ")
while True:

    command = input().split(" ")

    if command[0] == "Join":
        name = command[1]
        if name not in spl:
            a = spl.append(name)
            text = spl
        else:
            continue


    elif command[0] == "Jump":
        names = command[1]
        idx = int(command[2])
        if idx >= 0 and idx <= len(spl):
            h = spl.insert(idx, names)
            text = spl
        else:
            continue

    elif command[0] == "Dive":
        idx1 = int(command[1])
        if idx1 >= 0 and idx1 <= len(spl):
            s = spl.pop(idx1)
        else:
            continue

    elif command[0] == "First":
        count = int(command[1]) + 1
        if count >= 0 and count <= len(spl):
            ll = len(spl)
            mm = ll - count
            cutt = spl[:mm - 1]
            print(" ".join(cutt))

        else:
            p = " ".join(spl)
            print(p)

    elif command[0] == "Last":
        num_cut = int(command[1])
        if num_cut >= 0 and num_cut <= len(spl):
            l = len(spl)
            m = l - num_cut
            cut = spl[m:]
            print(" ".join(cut))

        else:
            p = " ".join(spl)
            print(p)


    elif command[0] == "Print" and command[1] == "Normal":
        p = " ".join(spl)
        print(f"Frogs: {p}")
        break

    elif command[0] == "Print" and command[1] == "Reversed":
        for i in reversed(spl):
            save.append(i)
        t = " ".join(save)
        print(f"Frogs: {t}")
        break
