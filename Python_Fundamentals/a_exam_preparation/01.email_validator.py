text = input()
new = "@"
dash = "-"
save = []
command = input()
while command != "Complete":
    conversion = command.split(" ")

    if conversion[0] == "Make":
        if conversion[1] == "Upper":
            conv = text.upper()    # правим всички букви големи
            text = conv            # сега големите букви ги запазваме в инпута

            print(conv)
        elif conversion[1] == "Lower":
            conv = text.lower()   # правим всички букви малки
            text = conv           # сега малките букви ги запазваме в инпута
            print(conv)

    elif conversion[0] == "GetDomain":
        number = int(conversion[1])
        cut = text[-number:text.rfind("")] # използваме функцията, за да изрежем думата.
        print(cut)                         # от MIKE123@SOMEMAIL.COM, остава MIKE123

    elif conversion[0] == "GetUsername":
        if new in text:             # за new(@) в текста, ако го има, влез.
            for letter in text:     # за буквата в текста
                if letter == "@":   # ако буквата е равна на @, влез и принирай резултата, събран в elsa, в масива save.
                    print("".join(save))
                    break
                else:
                    save.append(letter) # докато буквата не е равна на @, влизай и прехвърлай буквите в масива save.
        else:
            print(f"The email {text} doesn't contain the @ symbol.")


    elif conversion[0] == "Replace":
        new_letter = conversion[1]
        rev = text.replace(new_letter, dash) # заменяме символа new_letter(a), със силвола dash(-)
        print(rev)                       # anothermail.com --> -notherm-il.com

    elif conversion[0] == "Encrypt":
        for letter in text:            # за дубката в текста.
            ordd = ord(letter)         # после превръщаме буквите в числовата им стойност

            print(ordd, end=" ")

    command = input()
