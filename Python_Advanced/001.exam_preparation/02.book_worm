sentence = input()
n = int(input())
matrix = []
for i in range(n):
    matrix.append([x for x in input()])
command_num = int(input())
for i in range(command_num):
    cycle = True
    command = input()
    for c in range(len(matrix)):
        if not cycle:
            break
        for r in range(len(matrix[0])):
            if matrix[c][r] == "P":
                matrix[c][r] = '-'
                if command == 'up':
                    if c - 1 >= 0:
                        if matrix[c - 1][r].isalpha():
                            sentence += matrix[c - 1][r]
                            matrix[c - 1][r] = 'P'
                            cycle = False
                            break
                        else:
                            matrix[c - 1][r] = 'P'
                            cycle = False
                            break
                    else:
                        matrix[c][r] = 'P'
                        sentence = sentence[0:-1]
                        cycle = False
                        break
                elif command == 'down':
                    if c + 1 < len(matrix):
                        if matrix[c + 1][r].isalpha():
                            sentence += matrix[c + 1][r]
                            matrix[c + 1][r] = 'P'
                            cycle = False
                            break
                        else:
                            matrix[c + 1][r] = 'P'
                            cycle = False
                            break
                    else:
                        matrix[c][r] = 'P'
                        sentence = sentence[0:-1]
                        cycle = False
                        break
                elif command == 'left':
                    if r - 1 >= 0:
                        if matrix[c][r - 1].isalpha():
                            sentence += matrix[c][r - 1]
                            matrix[c][r - 1] = 'P'
                            cycle = False
                            break
                        else:
                            matrix[c][r - 1] = 'P'
                            cycle = False
                            break
                    else:
                        matrix[c][r] = 'P'
                        sentence = sentence[0:-1]
                        cycle = False
                        break
                elif command == 'right':
                    if r + 1 < len(matrix[0]):
                        if matrix[c][r + 1].isalpha():
                            sentence += matrix[c][r + 1]
                            matrix[c][r + 1] = 'P'
                            cycle = False
                            break
                        else:
                            matrix[c][r + 1] = 'P'
                            cycle = False
                            break
                    else:
                        matrix[c][r] = 'P'
                        sentence = sentence[0:-1]
                        cycle = False
                        break
print(sentence)
for i in matrix:
    print(''.join(i))
