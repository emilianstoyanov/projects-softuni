text = input()                          
count = -1
total = 0
save = []

command = input()                     
while command != "Finish":
    separation = command.split(" ")    

    if separation[0] == "Replace":
        first = separation[1]
        second = separation[2]
        rev = text.replace(separation[1], separation[2]) 
        text = rev           
        print(text)


    elif separation[0] == "Cut":
        first_cut = int(separation[1])   
        second_cut = int(separation[2])  
        len_word = len(text)            

        if first_cut >= 0 and second_cut <= len_word: 

            cuts = text[:first_cut]         
            save.append(cuts)

            cut = text[(second_cut + 1):]  
            save.append(cut)                   
            print("".join(save))

        else:
            print("Invalid indexes!")



    elif separation[0] == "Make":
        upper_lower = separation[1]
        if separation[1] == "Upper":
            upp = text.upper()        
            text = upp              
            print(text)
        elif separation[1] == "Lower":
            low = text.lower()    
            text = low               
            print(text)


    elif separation[0] == "Check":
        detect = separation[1]     
        if separation[1] in text:          
            print(f"Message contains {separation[1]}")
        else:
            print(f"Message doesn't contain {separation[1]}")


    elif separation[0] == "Sum":
        first_num = int(separation[1])   
        second_num = int(separation[2])  
        leght_max = len(text)            

        if first_num >= 0 and second_num <= leght_max: 

            for letter in text:
                count += 1 
                if count >= first_num and count <= second_num:
                    transf = ord(letter)
                    total += transf

            print(total)

        else:
            print("Invalid indexes!")

    command = input()
