text = input()

result = ""
current_string = ""

for i in range(len(text)):
    if text[i].isdigit():
        num = text[i]
        counter = i + 1
        while counter < len(text) and text[counter].isdigit():
            num += text[counter]
            counter += 1
        result += current_string.upper() * int(num)
        current_string = ""
    else:
        current_string += text[i]

print(f"Unique symbols used: {len(set(result))}")
print(result)
