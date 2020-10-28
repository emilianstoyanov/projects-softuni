def get_damage(row, col, matrix):
    counter = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row - 2][col - 1] == "K":
            counter += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row - 2][col + 1] == "K":
            counter += 1
    if row - 1 >= 0 and col - 2 >= 0:
        if matrix[row - 1][col - 2] == "K":
            counter += 1
    if row - 1 >= 0 and col + 2 < len(matrix):
        if matrix[row - 1][col + 2] == "K":
            counter += 1
    if row + 1 < len(matrix) and col - 2 >= 0:
        if matrix[row + 1][col - 2] == "K":
            counter += 1
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        if matrix[row + 1][col + 2] == "K":
            counter += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row + 2][col - 1] == "K":
            counter += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row + 2][col + 1] == "K":
            counter += 1
    return counter


rows_count = int(input())
matrix = []
position = []
deleted_knights = 0

for _ in range(rows_count):
    row = [x for x in input()]
    matrix.append(row)

while True:
    max_damage = 0
    for row_index in range(rows_count):
        for col_index in range(rows_count):
            current = matrix[row_index][col_index]
            if current == "K":
                damage = get_damage(row_index, col_index, matrix)
                if damage > max_damage:
                    max_damage = damage
                    position = [row_index, col_index]

    if max_damage == 0:
        break

    row = position[0]
    col = position[1]
    matrix[row][col] = "0"
    position = []
    deleted_knights += 1

print(deleted_knights)
