n = int(input())

unique_users = set()

for _ in range(n):
    username = input()

    unique_users.add(username)

[print(x) for x in unique_users]
