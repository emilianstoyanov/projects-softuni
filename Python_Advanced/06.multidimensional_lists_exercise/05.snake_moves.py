row, col = [int(x) for x in input().split()]

matrix = []
save_word = ''
text = input()
for c in range(col + 5):
    save_word += text

for r in range(row):
    matrix.append([])

    for let in save_word:
        if len(matrix[r]) < col:
            matrix[r].append(let)
        else:
            save_word = save_word[col:]
            break

rev = 0
for m in matrix:
    if rev % 2 == 0:
        print(''.join(m))
        rev += 1
    else:
        print(''.join(reversed(m)))
        rev += 1
