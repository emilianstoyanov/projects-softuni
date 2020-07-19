tail = input()
body = input()
head = input()

save = [tail, body, head]

# print([save[-1], save[-2], save[-3]])


correct_animal = save[::-1]
print(correct_animal)
