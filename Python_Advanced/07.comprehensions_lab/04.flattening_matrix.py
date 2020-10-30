def parse_row(string):
    return  map(int, string.split(", "))

rows = int(input())
matrix = [map(int, input().split(", ")) for _ in range(rows)]
flattend = [num for sublist in matrix for num in sublist]
print(flattend)
