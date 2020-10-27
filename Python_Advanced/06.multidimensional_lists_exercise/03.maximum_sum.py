count_rows, count_cols = [int(x) for x in input().split()]
matrix = []

total = -999999
best_matrix = []
for _ in range(count_rows):
    matrix.append([int(x) for x in input().split()])

for row in range(count_rows - 2):
    for col in range(count_cols - 2):
        moment_matrix = matrix[row][col]
        first_line = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]
        second_line = matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]
        third_line = matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        total_sum = first_line + second_line + third_line
        if total < total_sum:
            best_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                           [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                           [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

            total = total_sum

print(f"Sum = {total}")
for row in best_matrix:
    print(' '.join(str(x) for x in row))
