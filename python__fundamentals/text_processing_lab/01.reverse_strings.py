while True:

    text = input()

    if text == "end":
        break

    j = list(reversed(text))
    print(f"{text} = {''.join(j)}")
