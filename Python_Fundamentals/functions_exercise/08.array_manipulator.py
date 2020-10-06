import sys
 
 
def read_number_arr():
    input_arr = input().split()
    numbers = []
 
    for i in input_arr:
        numbers.append(int(i))
 
    return numbers
 
 
def exchange(numbers, index):
    new_arr = []
    for i in range(index + 1, len(numbers)):
        new_arr.append(numbers[i])
 
    for i in range(index + 1):
        new_arr.append(numbers[i])
 
    return new_arr
 
 
def max_num_index(numbers, type):
    best_max = -sys.maxsize
    best_index = -1
 
    if type == "even":
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0 and numbers[i] >= best_max:
                best_max = numbers[i]
                best_index = i
    elif type == "odd":
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0 and numbers[i] >= best_max:
                best_max = numbers[i]
                best_index = i
 
    return best_index
 
 
def min_num_index(numbers, type):
    best_min = sys.maxsize
    best_index = -1
 
    if type == "even":
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0 and numbers[i] <= best_min:
                best_min = numbers[i]
                best_index = i
    elif type == "odd":
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0 and numbers[i] <= best_min:
                best_min = numbers[i]
                best_index = i
 
    return best_index
 
 
def first_elements(numbers, count, type):
    new_arr = []
 
    if type == "odd":
        for i in range(len(numbers)):
            if numbers[i] % 2 != 0 and count > 0:
                new_arr.append(numbers[i])
                count -= 1
    elif type == "even":
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0 and count > 0:
                new_arr.append(numbers[i])
                count -= 1
 
    return new_arr
 
 
def last_elements(numbers, count, type):
    new_arr = []
 
    if type == "odd":
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] % 2 != 0 and count > 0:
                new_arr.append(numbers[i])
                count -= 1
    elif type == "even":
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] % 2 == 0 and count > 0:
                new_arr.append(numbers[i])
                count -= 1
 
    reversed_arr = []
 
    for i in range(len(new_arr) - 1, -1, -1):
        reversed_arr.append(new_arr[i])
 
    new_arr = reversed_arr
 
    return new_arr
 
 
def solve():
    numbers = read_number_arr()
    command_input = input()
 
    while command_input != "end":
        args = command_input.split()
        command = args[0]
 
        if command == "exchange":
            index = int(args[1])
 
            if index < 0 or index >= len(numbers):
                print("Invalid index")
                command_input = input()
                continue
 
            numbers = exchange(numbers, index)
        elif command == "max":
            type = args[1]
            max_index = max_num_index(numbers, type)
 
            if max_index != -1:
                print(max_index)
            else:
                print("No matches")
        elif command == "min":
            type = args[1]
            min_index = min_num_index(numbers, type)
 
            if min_index != -1:
                print(min_index)
            else:
                print("No matches")
        elif command == "first":
            count = int(args[1])
            type = args[2]
 
            if count > len(numbers):
                print("Invalid count")
                command_input = input()
                continue
 
            first_elements_arr = first_elements(numbers, count, type)
            print(first_elements_arr)
        elif command == "last":
            count = int(args[1])
            type = args[2]
 
            if count > len(numbers):
                print("Invalid count")
                command_input = input()
                continue
 
            last_elements_arr = last_elements(numbers, count, type)
            print(last_elements_arr)
 
        command_input = input()
 
    print(numbers)
 
 
solve()
