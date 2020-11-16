result_text = ""
with open("text.txt", "r") as file:
    for idx, line in enumerate(file):
        length = len([el for el in line if el.isalpha()])
        counter = 0
        for el in line:
            if el in "',.!?\";:-":
                counter += 1
        result_text += f"Line {idx + 1}: {line[:-2]} ({length})({counter})\n"

with open("output.txt", "w") as file:
    file.write(result_text)
