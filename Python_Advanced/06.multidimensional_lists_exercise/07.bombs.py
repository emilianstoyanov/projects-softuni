ize_matrix = int(input())

matrix = []
all_commands = []
for s in range(size_matrix):
    matrix.append([int(x) for x in input().split()])

coordinates = input().split(" ")

for x in coordinates:
    all_commands.append(x)

while all_commands:

    for command in all_commands:
        spl = command.split(",")
        row = int(spl[0])
        col = int(spl[1])

        moment_position = matrix[row][col]
        if matrix[row][col] <= 0:
            all_commands = all_commands[1:]
            continue

        if row - 1 >= 0:
            if matrix[row - 1][col] > 0:  # 2 отгоре
                matrix[row - 1][col] = matrix[row - 1][col] - moment_position

        if row - 1 >= 0 and col + 1 < len(matrix):
            if matrix[row - 1][col + 1] > 0:  # 5 горе дясо
                matrix[row - 1][col + 1] = matrix[row - 1][col + 1] - moment_position

        if row - 1 >= 0 and col - 1 >= 0:
            if matrix[row - 1][col - 1] > 0:  # 3 горе ляво
                matrix[row - 1][col - 1] = matrix[row - 1][col - 1] - moment_position

        if row + 1 < len(matrix):
            if matrix[row + 1][col] > 0:  # 3 отдолу
                matrix[row + 1][col] = matrix[row + 1][col] - moment_position

        if col - 1 >= 0:
            if matrix[row][col - 1] > 0:  # 4 ляво
                matrix[row][col - 1] = matrix[row][col - 1] - moment_position

        if col - 1 >= 0 and row + 1 < len(matrix):
            if matrix[row + 1][col - 1] > 0:  # 9 ляво долу
                matrix[row + 1][col - 1] = matrix[row + 1][col - 1] - moment_position

        if col + 1 < len(matrix):
            if matrix[row][col + 1] > 0:  # 9 дясно
                matrix[row][col + 1] = matrix[row][col + 1] - moment_position

        if col + 1 < len(matrix) and row + 1 < len(matrix):
            if matrix[row + 1][col + 1] > 0:  # 6 дясно долу
                matrix[row + 1][col + 1] = matrix[row + 1][col + 1] - moment_position

        matrix[row][col] = 0
        if all_commands:
            all_commands = all_commands[1:]
total = 0
count_alive = 0
for alive in matrix:
    for t in alive:
        if t > 0:
            total += t
            count_alive += 1

print(f"Alive cells: {count_alive}")
print(f"Sum: {total}")

for j in matrix:
    print(' '.join(str(x) for x in j))
