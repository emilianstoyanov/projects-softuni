save = []
savee= []
text = input().split(" ")
while True:

    command = input().split(" ")

    if command[0] == "Stop":
        print(" ".join(text))
        break

    elif command[0] == "Delete":
        idx_del = int(command[1])
        if idx_del >= 0 and idx_del + 1 < len(text):
            d = text.pop(idx_del + 1)
        else:
            continue


    elif command[0] == "Swap":
        word1 = command[1]
        word2 = command[2]
        if word1 in text and word2 in text:
            id1 = text.index(word1)
            id2 = text.index(word2)
            r = text[id1], text[id2] = text[id2], text[id1]
        else:
            continue


    elif command[0] == "Put":
        word = command[1]
        indexx = int(command[2]) - 1
        if indexx >= 0 and indexx <= len(text):
            if indexx == len(text):
                ap = text.append(word)
            else:
                i = text.insert(indexx, word)
        else:
            continue


    elif command[0] == "Sort":
        s = sorted(text)
        text = s



    elif command[0] == "Replace":
        first_word = command[1]
        second_word = command[2]

        if second_word in text:
            idd = text.index(second_word)
            l = text[idd] = first_word 
        else:
            continue
