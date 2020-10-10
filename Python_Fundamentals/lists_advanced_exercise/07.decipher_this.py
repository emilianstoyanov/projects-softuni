cypher = input().split()
answer = []
for i in cypher:
    result =  chr(int(''.join(list(filter(str.isdigit,i)))))
    reminder =''.join(list(filter(str.isalpha,i)))
    if len(reminder) <= 1:
        result += reminder
        answer.append(result)
    else:
        reminder = reminder[-1] + reminder[1:-1]+reminder[0]
        result += reminder
        answer.append(result)
print(' '.join(answer))
