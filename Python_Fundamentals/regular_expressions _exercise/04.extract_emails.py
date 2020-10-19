import re
pattern = r" ([a-zA-Z0-9]+[-\._]*[a-zA-Z0-9]+@[a-zA-Z]+-*[a-zA-Z]+([\.?][a-zA-Z]+-?[a-zA-Z]+)+)"

text = input()

matches = re.findall(pattern, text)

for match in matches:
    print(match[0])
