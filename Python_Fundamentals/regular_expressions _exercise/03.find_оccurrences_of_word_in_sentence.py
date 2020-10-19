import re
text = input()
word = input()

pattern = f"\\b{word}\\b"

matches = len(re.findall(pattern, text, re.I))

print(matches)
