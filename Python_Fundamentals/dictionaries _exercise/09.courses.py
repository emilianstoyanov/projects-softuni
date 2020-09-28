reg = {}

while True:
    text = input().split(" : ")
    if text[0] == "end":
        break

    course = text[0]
    name = text[1]

    if course not in reg:
        reg[course] = []
    reg[course].append(name)

sorted_dict = dict(sorted(reg.items(), key=lambda x: (-len(x[1]))))

for (key, value) in sorted_dict.items():
    if len(value) > 0:
        print(f"{key}: {len(value)}")
        [print(f"-- {name}") for name in sorted(value)]








# reg = {}
#
# while True:
#     text = input().split(" : ")
#     if text[0] == "end":
#         break
#
#     course = text[0]
#     name = text[1]
#
#     if course not in reg:
#         reg[course] = []
#     reg[course].append(name)
#
# sorted_dict = dict(sorted(reg.items(), key=lambda x: (-len(x[1]))))
#
# for (key, value) in sorted_dict.items():
#     if len(value) > 0:
#         print(f"{key}: {len(value)}")
#         [print(f"-- {name}") for name in sorted(value)]

# [print(f"! {user}") for user in sorted(value)]
