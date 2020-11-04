number_strings = input()
spl = number_strings.split(" ")  # --> ['73', 114, '111', '116', '114', '101', '115']
while True:


    command = input().split(" ")

    if command[0] == "END":
        total = " ".join(map(str, spl))  # --> 73 114 111 116 114 101 115    МАХА СКОБИ И ЗАПЕТАИ
        print(total)
        break


    elif command[0] == "Reverse":
            rev = reversed(spl)    # ОБРЪЩА ТЕКСА ОБРАТНО
            number = list(rev)
            spl = number


    elif command[0] == "Change":
        fist_num = command[1]
        second_num = command[2]
        if fist_num in spl:      # ако числото (стринг) го има в текста
            index = spl.index(fist_num)
            rep = spl[index] = command[2]   # размени местата на първото с второто


        else:
            continue


    elif command[0] == "Hide":
        one = command[1]
        if one in spl:  # ако елемента присъста
            rem = spl.remove(one) 

        else:
            continue


    elif command[0] == "Switch":
        num1 = command[1]
        num2 = command[2]
        if num1 in spl and num2 in spl:    
            a, b = spl.index(num1), spl.index(num2)
            rev = spl[a], spl[b] = spl[b], spl[a] 
        else:
            continue


    elif command[0] == "Insert":
        index = int(command[1])    
        impl_num = int(command[2])       
        if index >= 0 and index <= len(spl):      
            if command[2] in spl:
                textt = spl.insert(index + 1, impl_num)  
            else:
                textt = spl.insert(index + 1, impl_num)
        else:
            continue




