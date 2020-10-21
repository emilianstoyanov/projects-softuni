from collections import deque
 
green_light = int(input())
free_window = int(input())
 
command = input()
success = True
passed_cars = 0
cars = deque()
 
while command != 'END':
 
    if command != 'green':
        cars.append(command)
 
    elif cars:
        current_green = green_light
        current_free_window = free_window
 
        while cars:
            if current_green <= 0:
                break
            current_car = len(cars[0])
 
            if current_green > 0:
                stamp_of_green_left_if_crash = current_green
                current_green -= current_car
 
                if current_green < 0:
                    current_car = -1 * current_green
                    current_free_window -= current_car
 
                    if current_free_window < 0:
                        success = False
                        letter_index = stamp_of_green_left_if_crash + free_window
                        letter = cars[0][letter_index]
                        print('A crash happened!')
                        print(f'{cars[0]} was hit at {letter}.')
                        break
 
                    else:
                        cars.popleft()
                        passed_cars += 1
 
                else:
                    cars.popleft()
                    passed_cars += 1
 
    if not success:
        break
 
    command = input()
 
if success:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')
