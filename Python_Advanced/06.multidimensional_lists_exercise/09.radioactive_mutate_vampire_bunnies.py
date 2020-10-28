def move_player(current_pos, next_pos, matrix):
    has_won = False
    if next_pos[0] >= 0 and next_pos[0] < len(matrix) and next_pos[1] >= 0 and next_pos[1] < len(matrix[0]):
        if matrix[next_pos[0]][next_pos[1]] == ".":
            matrix[next_pos[0]][next_pos[1]] = "P"
            matrix[current_pos[0]][current_pos[1]] = "."
        else:
            matrix[current_pos[0]][current_pos[1]] = "P"
    else:
        matrix[current_pos[0]][current_pos[1]] = "."
        has_won = True
    return has_won
 
def get_bunny_possitions(matrix):
    bunny_possitions = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "B":
                bunny_possitions.append([row, col])
    return bunny_possitions
 
def mutate_bunnies(bunny_possitions, matrix):
    is_dead = False
    for [row, col] in bunny_possitions:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i + j != 0 and i != j:
                    if row + i >= 0 and row + i < len(matrix) and col + j >= 0 and col + j < len(matrix[row]):
                        if matrix[row+i][col+j] == ".":
                            matrix[row+i][col+j] = "B"
                        elif matrix[row+i][col+j] == "P":
                            matrix[row+i][col+j] = "B"
                            is_dead = True
    return is_dead
 
rows, cols = [int(x) for x in input().split()]
matrix = []
player_pos = []
is_dead = False
 
for row in range(rows):
    line = [x for x in input()]
    if "P" in line:
        player_pos = [row, line.index("P")]
    matrix.append(line)
 
commands = input()
 
for command in commands:
    next_pos = []
 
    if command == "U":
        next_pos = [player_pos[0] - 1, player_pos[1]]
    elif command == "D":
        next_pos = [player_pos[0] + 1, player_pos[1]]
    elif command == "L":
        next_pos = [player_pos[0], player_pos[1] - 1]
    elif command == "R":
        next_pos = [player_pos[0], player_pos[1] + 1]
 
    has_won = move_player(player_pos, next_pos, matrix)
    bunny_possitions = get_bunny_possitions(matrix)
    is_dead = mutate_bunnies(bunny_possitions, matrix)
 
    if has_won:
        for row in matrix:
            print(''.join(row))
        print(f"won: {player_pos[0]} {player_pos[1]}")
        break
   
    player_pos = next_pos
 
    if is_dead:
        for row in matrix:
            print(''.join(row))
        print(f"dead: {player_pos[0]} {player_pos[1]}")
        break
