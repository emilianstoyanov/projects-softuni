first_number = int(input())
second_number = int(input())

while first_number <= second_number:
    conversion = chr(first_number)
    first_number += 1
    print(conversion, end=' ')
