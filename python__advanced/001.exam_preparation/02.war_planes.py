size_matrix = int(input())

matrix = []
row = 0
col = 0
count_t = 0
final_t = 0
for i in range(size_matrix):
    matrix.append([x for x in input().split()])

for search_p in matrix:
    if "p" in search_p:
        col = search_p.index("p")
        break
    else:
        row += 1

for search_p in matrix:
    for f in search_p:
        if f == "t":
            final_t += 1



moment_position = matrix[row][col]

all_commands = []
count_command = int(input())
for com in range(count_command):
    commands = input().split(" ")
    all_commands.append(commands)

for c in all_commands:
    move_shoot = c[0]
    position = c[1]
    steps = int(c[2])

    if move_shoot == "move":
        if position == "down":
            if row + steps < len(matrix) and matrix[row + steps][col] == ".":
                matrix[row + steps][col] = "p"
                matrix[row][col] = "."
                row += steps

        elif position == "left":
            if col - steps >= 0 and matrix[row][col - steps] == ".":
                matrix[row][col - steps] = "p"
                matrix[row][col] = "."
                col -= steps

        elif position == "right":
            if col + steps < len(matrix) and matrix[row][col + steps] == ".":
                matrix[row][col + steps] = "p"
                matrix[row][col] = "."
                col += steps

        elif position == "up":
            if row - steps >= 0 and matrix[row - steps][col] == ".":
                matrix[row - steps][col] = "p"
                matrix[row][col] = "."
                row -= steps


    elif move_shoot == "shoot":
        if position == "down":
            if row + steps < len(matrix):
                if matrix[row + steps][col] == "t":
                    matrix[row + steps][col] = "x"
                    count_t += 1
                else:
                    matrix[row + steps][col] = "x"


        elif position == "left":
            if col - steps >= 0:
                if matrix[row][col - steps] == "t":
                    matrix[row][col - steps] = "x"
                    count_t += 1
                else:
                    matrix[row][col - steps] = "x"

        elif position == "right":
            if col + steps < len(matrix):
                if matrix[row][col + steps] == "t":
                    matrix[row][col + steps] = "x"
                    count_t += 1
                else:
                    matrix[row][col + steps] = "x"

        elif position == "up":
            if row - steps >= 0:
                if matrix[row - steps][col] == "t":
                    matrix[row - steps][col] = "x"
                    count_t += 1
                else:
                    matrix[row - steps][col] = "x"

    if count_t == final_t:
        print(f"Mission accomplished! All {count_t} targets destroyed.")
        break


if final_t > count_t:
    print(f"Mission failed! {final_t - count_t} targets left.")


for x in matrix:
    print(' '.join(x))
