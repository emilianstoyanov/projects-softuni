size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(len(matrix)):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][size - i - 1]

total = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(total)
