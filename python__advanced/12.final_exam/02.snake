size_matrix = int(input())
matrix = []

pls = []

for i in range(size_matrix):
    matrix.append([x for x in input()])

for row in range(size_matrix):
    for col in range(size_matrix):
        if matrix[row][col] == 'B':
            pls.append((row, col))

count_food = 0
for row in range(size_matrix):
    for col in range(size_matrix):
        if matrix[row][col] == '*':
            count_food += 1

row_s = 0
col_s = 0

for search_s in matrix:
    if "S" in search_s:
        col_s = search_s.index("S")
        break
    else:
        row_s += 1

first_position_s = matrix[row_s][col_s]
countar_stop_food = 0
if pls:
    exit_B_row = int(pls[1][0])
    exit_B_col = int(pls[1][1])

while True:
    command = input()
    if not command:
        break


    if command == "up":
        if row_s - 1 >= 0:
            if matrix[row_s - 1][col_s] == "B":
                matrix[row_s][col_s] = "."
                matrix[row_s - 1][col_s] = "."

                matrix[exit_B_row][exit_B_col] = "S"
                row_s = exit_B_row
                col_s = exit_B_col


            elif matrix[row_s - 1][col_s] == "*":
                matrix[row_s][col_s] = "."
                matrix[row_s - 1][col_s] = "S"
                countar_stop_food += 1
                row_s -= 1
                if countar_stop_food == 10:
                    print("You won! You fed the snake.")
                    print("Food eaten: 10")
                    for d in matrix:
                        print(''.join(d))
                    exit()

            elif matrix[row_s - 1][col_s] == "-":
                matrix[row_s - 1][col_s] = "S"
                matrix[row_s][col_s] = "."
                row_s -= 1
        else:
            matrix[row_s][col_s] = "."
            print("Game over!")
            print(f"Food eaten: {countar_stop_food}")
            for d in matrix:
                print(''.join(d))
            exit()

    elif command == "down":
        if row_s + 1 < len(matrix):
            if matrix[row_s + 1][col_s] == "B":
                matrix[row_s][col_s] = "."
                matrix[row_s + 1][col_s] = "."

                matrix[exit_B_row][exit_B_col] = "S"
                row_s = exit_B_row
                col_s = exit_B_col


            elif matrix[row_s + 1][col_s] == "*":
                matrix[row_s][col_s] = "."
                matrix[row_s + 1][col_s] = "S"
                countar_stop_food += 1
                row_s += 1
                if countar_stop_food == 10:
                    print("You won! You fed the snake.")
                    print("Food eaten: 10")
                    for d in matrix:
                        print(''.join(d))
                    exit()

            elif matrix[row_s + 1][col_s] == "-":
                matrix[row_s + 1][col_s] = "S"
                matrix[row_s][col_s] = "."
                row_s += 1
        else:
            matrix[row_s][col_s] = "."
            print("Game over!")
            print(f"Food eaten: {countar_stop_food}")
            for d in matrix:
                print(''.join(d))
            exit()


    elif command == "left":
        if col_s - 1 >= 0:
            if matrix[row_s][col_s - 1] == "B":
                matrix[row_s][col_s] = "."
                matrix[row_s][col_s - 1] = "."

                matrix[exit_B_row][exit_B_col] = "S"
                row_s = exit_B_row
                col_s = exit_B_col


            elif matrix[row_s][col_s - 1] == "*":
                matrix[row_s][col_s] = "."
                matrix[row_s][col_s - 1] = "S"
                countar_stop_food += 1
                col_s -= 1
                if countar_stop_food == 10:
                    print("You won! You fed the snake.")
                    print("Food eaten: 10")
                    for d in matrix:
                        print(''.join(d))
                    exit()

            elif matrix[row_s][col_s - 1] == "-":
                matrix[row_s][col_s - 1] = "S"
                matrix[row_s][col_s] = "."
                col_s -= 1
        else:
            matrix[row_s][col_s] = "."
            print("Game over!")
            print(f"Food eaten: {countar_stop_food}")
            for l in matrix:
                print(''.join(l))
            exit()



    elif command == "right":
        if col_s + 1 < len(matrix):
            if matrix[row_s][col_s + 1] == "B":
                matrix[row_s][col_s] = "."
                matrix[row_s][col_s + 1] = "."

                matrix[exit_B_row][exit_B_col] = "S"
                row_s = exit_B_row
                col_s = exit_B_col

            elif matrix[row_s][col_s + 1] == "*":
                matrix[row_s][col_s] = "."
                matrix[row_s][col_s + 1] = "S"
                countar_stop_food += 1
                col_s += 1
                if countar_stop_food == 10:
                    print("You won! You fed the snake.")
                    print("Food eaten: 10")
                    for r in matrix:
                        print(''.join(r))
                    exit()

            elif matrix[row_s][col_s + 1] == "-":
                matrix[row_s][col_s + 1] = "S"
                matrix[row_s][col_s] = "."
                col_s += 1
        else:
            matrix[row_s][col_s] = "."
            print("Game over!")
            print(f"Food eaten: {countar_stop_food}")
            for r in matrix:
                print(''.join(r))
            exit()
