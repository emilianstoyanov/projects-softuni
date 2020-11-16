count_gifts = int(input())
size_matrix = int(input())

matrix = []
count_nice_kids = 0
row = 0
col = 0
kids = []

for m in range(size_matrix):
    matrix.append([x for x in input().split()])

for santa in matrix:
    if "S" in santa:
        col = santa.index("S")
        break
    else:
        row += 1

first_position_santa = matrix[row][col]
command = input()
while command != "Christmas morning" and count_gifts >= 0:

    if command == "up":
        if row - 1 >= 0:
            if matrix[row - 1][col] == "X":
                matrix[row][col] = "-"
                matrix[row - 1][col] = "S"
                row -= 1

            elif matrix[row - 1][col] == "V":
                matrix[row][col] = "-"
                matrix[row - 1][col] = "S"
                count_nice_kids += 1
                row -= 1
            elif matrix[row - 1][col] == "C":
                row -= 1
                matrix[row][col] = "S"
                kids.append(matrix[row - 1][col])
                matrix[row - 1][col] = "-"
                # kids.append(matrix[row + 1][col])
                matrix[row + 1][col] = "-"
                kids.append(matrix[row][col - 1])
                matrix[row][col - 1] = "-"
                kids.append(matrix[row][col + 1])
                matrix[row][col + 1] = "-"
                for c in kids:
                    if c != "-":
                        count_gifts -= 1


            elif matrix[row - 1][col] == "-":
                matrix[row - 1][col] = "S"
                matrix[row][col] = "-"
                row -= 1

    elif command == "down":
        if row + 1 < len(matrix):
            if matrix[row + 1][col] == "X":
                matrix[row][col] = "-"
                matrix[row + 1][col] = "S"
                row += 1

            elif matrix[row + 1][col] == "V":
                matrix[row][col] = "-"
                matrix[row + 1][col] = "S"
                count_nice_kids += 1
                row += 1

            elif matrix[row + 1][col] == "C":
                row += 1
                matrix[row][col] = "S"
                # kids.append(matrix[row - 1][col])
                matrix[row - 1][col] = "-"
                kids.append(matrix[row + 1][col])
                matrix[row + 1][col] = "-"
                kids.append(matrix[row][col - 1])
                matrix[row][col - 1] = "-"
                kids.append(matrix[row][col + 1])
                matrix[row][col + 1] = "-"
                for c in kids:
                    if c != "-":
                        count_gifts -= 1

            elif matrix[row + 1][col] == "-":
                matrix[row + 1][col] = "S"
                matrix[row][col] = "-"
                row += 1

    elif command == "right":
        if col + 1 < len(matrix):
            if matrix[row][col + 1] == "X":
                matrix[row][col] = "-"
                matrix[row][col + 1] = "S"
                col += 1
            elif matrix[row][col + 1] == "V":
                matrix[row][col] = "-"
                matrix[row][col + 1] = "S"
                count_nice_kids += 1
                col += 1
            elif matrix[row][col + 1] == "C":
                col += 1
                matrix[row][col] = "S"
                kids.append(matrix[row - 1][col])
                matrix[row - 1][col] = "-"
                kids.append(matrix[row + 1][col])
                matrix[row + 1][col] = "-"
                # kids.append(matrix[row][col - 1])
                matrix[row][col - 1] = "-"
                kids.append(matrix[row][col + 1])
                matrix[row][col + 1] = "-"
                for c in kids:
                    if c != "-":
                        count_gifts -= 1

            elif matrix[row][col + 1] == "-":
                matrix[row][col + 1] = "S"
                matrix[row][col] = "-"
                col += 1

    elif command == "left":
        if col - 1 >= 0:
            if matrix[row][col - 1] == "X":
                matrix[row][col] = "-"
                matrix[row][col - 1] = "S"
                col -= 1

            elif matrix[row][col - 1] == "V":
                matrix[row][col] = "-"
                matrix[row][col - 1] = "S"
                count_nice_kids += 1
                col -= 1
            elif matrix[row][col - 1] == "C":
                col -= 1
                matrix[row][col] = "S"
                matrix[row - 1][col] = "-"
                matrix[row + 1][col] = "-"
                matrix[row][col - 1] = "-"
                matrix[row][col + 1] = "-"
                count_gifts -= 4

            elif matrix[row][col - 1] == "-":
                matrix[row][col - 1] = "S"
                matrix[row][col] = "-"
                col -= 1
    if count_gifts <= 0:
        break

    command = input()

if count_gifts <= 0:
    for t in matrix:
        if "V" in t:
            print("Santa ran out of presents!")
            break

for j in matrix:
    print(' '.join(j))

good_kids = 0
for h in matrix:
    if "V" in h:
        good_kids += 1

if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
