companies = {}

while True:
    command = input()

    if command == "End":
        break

    spl_command = command.split(" -> ")
    name = spl_command[0]
    id = spl_command[1]

    if name not in companies:
        companies[name] = []
        companies[name].append(id)
    else:
        if id in companies[name]:
            continue
        else:
            companies[name].append(id)

sort_companies = dict(sorted(companies.items(), key=lambda x: x[0]))

for k, v in sort_companies.items():
    print(k)
    for i in v:
        print(f"-- {i}")


#
# d = {}
#
# command = input()
# while command != "End":
#     text = command.split(" -> ")
#
#     company_name = text[0]
#     id = text[1]
#
#     if company_name not in d:
#         d[company_name] = [id]
#
#     else:
#         if id in d[company_name]:
#             command = input()
#             continue
#         else:
#             d[company_name] += [id]
#
#     command = input()
# sorted_dict = dict(sorted(d.items(), key=lambda x: x[0]))
# for (key, value) in sorted_dict.items():
#     print(key)
#     for i in value:
#         print(f"-- {i}")
#

