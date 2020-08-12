rows_count, cols_count = [int(x) for x in input().split()]
matrix = []
counter = 0
for _ in range(rows_count):
    matrix.append(input().split())

for row in range(rows_count - 1):
    for col in range(cols_count - 1):
        current = matrix[row][col]
        to_the_right = matrix[row][col + 1]
        to_the_bottom = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]
        if current == to_the_right == to_the_bottom == bottom_right:
            counter += 1

print(counter)