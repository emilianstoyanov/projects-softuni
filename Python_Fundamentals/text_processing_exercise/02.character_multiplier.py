input_text = input().split(" ")

first_string = input_text[0]
second_string = input_text[1]

total_sum = 0

for i in range(max(len(first_string), len(second_string))):
    if i < len(first_string) and i < len(second_string):
        total_sum += ord(first_string[i]) * ord(second_string[i])
    else:
        if i < len(first_string):
            total_sum += ord(first_string[i])

        else:
            total_sum += ord(second_string[i])

print(total_sum)
