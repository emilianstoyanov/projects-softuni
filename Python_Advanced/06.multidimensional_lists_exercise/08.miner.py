size = int(input())
commands = input().split()
miner_position = []
coals = 0
total_coals = 0

end = False
matrix = []
for i in range(size):
    row = input().split()
    matrix.append(row)
    if "s" in row:
        miner_position = [i, row.index("s")]
    total_coals += row.count("c")


for command in commands:
    next_miner_position = []
    if command == "up":
        next_miner_position = [miner_position[0] - 1, miner_position[1]]
    elif command == "down":
        next_miner_position = [miner_position[0] + 1, miner_position[1]]
    elif command == "left":
        next_miner_position = [miner_position[0], miner_position[1] - 1]
    elif command == "right":
        next_miner_position = [miner_position[0], miner_position[1] + 1]

    if 0 <= next_miner_position[0] < len(matrix) and 0 <= next_miner_position[1] < len(matrix):
        row = next_miner_position[0]
        col = next_miner_position[1]
        if matrix[row][col] == "*":
            matrix[miner_position[0]][miner_position[1]] = "*"
            matrix[row][col] = "s"
            miner_position = next_miner_position
        elif matrix[row][col] == "e":
            print(f"Game over! ({row}, {col})")
            end = True
            break
        elif matrix[row][col] == "c":
            coals += 1
            if coals == total_coals:
                print(f"You collected all coals! ({row}, {col})")
                end = True
                break
            matrix[miner_position[0]][miner_position[1]] = "*"
            matrix[row][col] = "s"
            miner_position = next_miner_position


if not end:
    print(f"{total_coals - coals} coals left. ({miner_position[0]}, {miner_position[1]})")
