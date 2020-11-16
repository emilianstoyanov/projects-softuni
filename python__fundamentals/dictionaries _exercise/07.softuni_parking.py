count = int(input())

reg = {}

for i in range(count):
    text = input().split(" ")

    if text[0] == "register":

        if text[1] in reg and reg[text[1]] == text[2]:
            print(f"ERROR: already registered with plate number {text[2]}")
            continue

        if text[1] not in reg:
            reg[text[1]] = []
        reg[text[1]] = text[2]
        print(f"{text[1]} registered {text[2]} successfully")

    elif text[0] == "unregister":
        if text[1] not in reg:
            print(f"ERROR: user {text[1]} not found")
        else:
            del reg[text[1]]
            print(f"{text[1]} unregistered successfully")

for (key, value) in reg.items():
    print(f"{key} => {value}")
