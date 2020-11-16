d = {}

language_dict = {}
while True:
    text = input()
    if text == "exam finished":
        break

    spl = text.split("-")
    if spl[1] == "banned":
        if spl[0] in d:
            del d[spl[0]]
            continue

    name = spl[0]
    language = spl[1]
    points = int(spl[2])

    if name not in d:
        d[name] = {language: points}
        if language not in language_dict:
            language_dict[language] = 1
        else:
            language_dict[language] += 1

    elif name in d:
        if language in d[name]:
            if d[name][language] < points:
                d[name][language] = points
            if language not in language_dict:
                language_dict[language] = 1
            else:
                language_dict[language] += 1
        else:
            d[name].update({language: points})
            if language not in language_dict:
                language_dict[language] = 1
            else:
                language_dict[language] += 1


print("Results:")
for key, value in sorted(d.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{key} | {sum(value.values())}")

print("Submissions:")
for k, v in sorted(language_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k} - {v}")
