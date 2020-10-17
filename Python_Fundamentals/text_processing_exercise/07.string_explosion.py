text = input()
result = ""
i = 0
count = 0

while i < len(text):
    if text[i] != ">":
        result += text[i]
        i += 1
    else:
        result += ">"
        i += 1
        count += int(text[i])
        while count > 0 and text[i] != ">":
            i += 1
            count -= 1
            if i >= len(text):
                break

print(result)
