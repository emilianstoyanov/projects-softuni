contests = {}
users = {}
line = input()

while line != "no more time":
    tokens = line.split(" -> ")
    username = tokens[0]
    course = tokens[1]
    points = int(tokens[2])
    if course not in contests:
        contests[course] = {}
    if username not in contests[course]:
        contests[course][username] = points
    elif contests[course][username] < points:
        contests[course][username] = points
    line = input()

for course in contests.values():
    for user in course.items():
        if user[0] not in users:
            users[user[0]] = 0
        users[user[0]] += user[1]

for key in sorted(contests, key=lambda x: -len(contests[x].keys())):
    print(f"{key}: {len(contests[key].items())} participants")
    sorted_contents = list(sorted(contests[key].items(), key=lambda x: -x[1]))
    for i in range(len(sorted_contents)):
        print(f"{i + 1}. {sorted_contents[i][0]} <::> {sorted_contents[i][1]}")

print("Individual standings:")
sorted_users = list(sorted(users.items(), key=lambda x: -x[1]))
for i in range(len(sorted_users)):
    print(f"{i + 1}. {sorted_users[i][0]} -> {sorted_users[i][1]}")

