n = int(input())

left_chairs = 0
enough_chairs = True
for i in range(1, n + 1):
    tokens = input().split(" ")
    chairs = len(tokens[0])
    people = int(tokens[1])
    if chairs >= people:
        left_chairs += chairs - people
    else:
        enough_chairs = False
        print(f"{people - chairs} more chairs needed in room {i}")

if enough_chairs:
    print(f"Game On, {left_chairs} free chairs left")
