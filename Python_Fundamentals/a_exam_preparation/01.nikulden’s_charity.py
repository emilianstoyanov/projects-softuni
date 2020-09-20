text = input()                           # "ILikeSharan"
count = -1
total = 0
save = []

command = input()                         # command: "Replace a e"
while command != "Finish":
    separation = command.split(" ")     # separation["Replace", "a", "e"]

    if separation[0] == "Replace":
        first = separation[1]
        second = separation[2]
        rev = text.replace(separation[1], separation[2]) # заменяме символите [1] с [2] с функц. .replace
        text = rev            # прехвърляме стойността със сменените символи в инпута
        print(text)


    elif separation[0] == "Cut":
        first_cut = int(separation[1])   # 1
        second_cut = int(separation[2])  # 4
        len_word = len(text)             # 11

        if first_cut >= 0 and second_cut <= len_word: # 1 да е >= от нула, 4 по-малко или равно от дължината,Len

            cuts = text[:first_cut]         # от ILIKESHEREN остава I.
            save.append(cuts)

            cut = text[(second_cut + 1):]       # от ILIKESHEREN остава SHEREN
            save.append(cut)                     # вкарваме в масива I и SHEREN

            print("".join(save))

        else:
            print("Invalid indexes!")



    elif separation[0] == "Make":
        upper_lower = separation[1]
        if separation[1] == "Upper":
            upp = text.upper()         # прави всички символи големи
            text = upp                 # пренасяме вече големите букви в инпута
            print(text)
        elif separation[1] == "Lower":
            low = text.lower()       # прави всички символи малки
            text = low               # пренасяме вече смалените букви в инпута
            print(text)


    elif separation[0] == "Check":
        detect = separation[1]      # SHEREN
        if separation[1] in text:           # ако в текста има SHEREN , принтирай съобщението
            print(f"Message contains {separation[1]}")
        else:
            print(f"Message doesn't contain {separation[1]}")


    elif separation[0] == "Sum":
        first_num = int(separation[1])   # 1
        second_num = int(separation[2])  # 4
        leght_max = len(text)            # 11

        if first_num >= 0 and second_num <= leght_max:  # 0 - 11 , ако числата са в този диапазон, влез.

            for letter in text:
                count += 1  # да сумираме стойностите от числовите сойности зад буквите от 1 до 4, count започва от -1.
                if count >= first_num and count <= second_num: # влизай, докато count е в диапазона, започваме от -1. 0
                    transf = ord(letter)
                    total += transf

            print(total)

        else:
            print("Invalid indexes!")

    command = input()
