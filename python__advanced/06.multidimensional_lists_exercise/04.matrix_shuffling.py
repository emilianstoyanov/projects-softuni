row, col = [int(x) for x in input().split()]

matrix = []

for i in range(row):
    matrix.append([x for x in input().split()])

all_commands = []
while True:

    commands = input().split()

    if commands[0] == "END":
        break

    if commands[0] == "swap" and len(commands) == 5:
        row_one = int(commands[1])
        col_one = int(commands[2])

        row_two = int(commands[3])
        col_two = int(commands[4])

        if row_one >= 0 and row_one <= row - 1 and col_one >= 0 and col_one <= col - 1:
            if row_two >= 0 and row_two <= row - 1 and col_two >= 0 and col_two <= col - 1:
                first = matrix[row_one][col_one]
                second = matrix[row_two][col_two]

                matrix[row_one][col_one] = second
                matrix[row_two][col_two] = first
                for t in matrix:
                    print(' '.join(t))
                continue

            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
