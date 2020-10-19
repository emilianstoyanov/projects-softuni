import re

pattern = r"\b_{1}[a-zA-Z0-9]+\b"

text = input()
matches = [x.replace("_","") for x in re.findall(pattern, text)]
print(",".join(matches))
