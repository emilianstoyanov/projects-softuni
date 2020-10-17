text = input()

i = 0

while i < len(text) - 1:
    if text[i] == text[i + 1]:
        text = text.replace(f"{text[i]}{text[i+1]}", f"{text[i]}")
    else:
        i += 1

print(text)
