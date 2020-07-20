text = input()
while True:
    spl = input().split(">>>")
    if spl[0] == "Generate":
        print(f"Your activation key is: {text}")
        break

    command = spl[0]
    if command == "Contains":
        substring = spl[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        if spl[1] == "Upper":
            f_inx = int(spl[2])
            s_idx = int(spl[3])
            ss = text[f_inx: s_idx].upper()
            text = text.replace(text[f_inx: s_idx], ss)
            print(text)

        elif spl[1] == "Lower":
            f_inx = int(spl[2])
            s_idx = int(spl[3])
            ss = text[f_inx: s_idx].lower()
            text = text.replace(text[f_inx: s_idx], ss)
            print(text)

    elif command == "Slice":
        first = int(spl[1])
        second = int(spl[2])
        cut = text[first:second]
        text = text.replace(text[first: second], "")
        print(text)
