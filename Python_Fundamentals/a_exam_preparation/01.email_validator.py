text = input()
new = "@"
dash = "-"
save = []
command = input()
while command != "Complete":
    conversion = command.split(" ")

    if conversion[0] == "Make":
        if conversion[1] == "Upper":
            conv = text.upper()    
            text = conv           

            print(conv)
        elif conversion[1] == "Lower":
            conv = text.lower()   
            text = conv         
            print(conv)

    elif conversion[0] == "GetDomain":
        number = int(conversion[1])
        cut = text[-number:text.rfind("")] 
        print(cut)                         

    elif conversion[0] == "GetUsername":
        if new in text:             
            for letter in text:   
                if letter == "@":  
                    print("".join(save))
                    break
                else:
                    save.append(letter) 
        else:
            print(f"The email {text} doesn't contain the @ symbol.")


    elif conversion[0] == "Replace":
        new_letter = conversion[1]
        rev = text.replace(new_letter, dash) 
        print(rev)                     
    elif conversion[0] == "Encrypt":
        for letter in text:          
            ordd = ord(letter)        

            print(ordd, end=" ")

    command = input()
