from collections import deque


def get_magic_triangle(n):
    magic_triangle = []
    moment_save = deque()
    count_first = 0
    for i in range(n):
        magic_triangle.append([])

        if i == 0:
            magic_triangle[i].append(1)
        elif i == 1:
            magic_triangle[i].append(1)
            magic_triangle[i].append(1)
            moment_save += magic_triangle[-1]
        else:
            while moment_save:

                if count_first == 0:
                    magic_triangle[i].append(1)
                    count_first += 1

                first = moment_save.popleft()
                second = moment_save.popleft()
                s = first + second


                if len(moment_save) > 0:
                    moment_save.appendleft(second)
                    magic_triangle[i].append(s)


                if len(moment_save) == 0:
                    magic_triangle[i].append(s)
                    magic_triangle[i].append(1)
                    moment_save += magic_triangle[-1]
                    count_first = 0
                    break

    return magic_triangle
