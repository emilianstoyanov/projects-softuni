import re
input_str = input()
p = r"(\*{2}|:{2})([A-Z]{1}[a-z]{2,})(\1)"

save = []
for i in input_str:
    preo = str(i)
    if preo.isdigit():
        save.append(int(i))

tr_shold = save[0]
prom = save[1:]
for intt in prom:
    tr_shold *= intt

print(f"Cool threshold: {tr_shold}")
match = re.findall(p, input_str)

if match:
    print(f"{len(match)} emojis found in the text. The cool ones are:")

    for j in match:
        number = 0
        pp = j[1]
        for searsh in pp:
            trans = ord(searsh)
            number += trans
        if number > tr_shold:
            jon = ''.join(j)
            print(jon)
