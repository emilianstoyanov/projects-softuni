import re

pattern = r"\d+"

while True:
    line = input()
    if not line:
        break
    matches = re.findall(pattern, line)
    for match in matches:
        print(match, end=" ")
