fyrst_number = int(input())
second_number = int(input())
third_number = int(input())

if fyrst_number > second_number and fyrst_number > third_number:
    print(fyrst_number)

elif second_number > fyrst_number and second_number > third_number:
    print(second_number)

else:
    print(third_number)
