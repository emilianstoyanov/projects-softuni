first_sort = {}
second_sort = {}
save = []  # 01. Ranking  чака за поправка
count_save = 0
save_total_sum = 0
moment_total_sum = 0
save_win_name = ""
count = 0
text = input()
while True:
    if text == "end of contests":
        text = input()
        continue

    if text == "end of submissions":
        for k, v in second_sort.items():
            for j in v.values():
                moment_total_sum += j

            if moment_total_sum > save_total_sum:
                save_total_sum = moment_total_sum
                save_win_name = k
                moment_total_sum = 0

        print(f"Best candidate is {save_win_name} with total {save_total_sum} points.")
        print("Ranking:")
        for key, value in sorted(second_sort.items(), key=lambda x: x[0]):

            print(f"{key}")

            sorted_dict = dict(sorted(value.items(), key=lambda k: k[1], reverse=True))
            for it, num in sorted_dict.items():
                print(f"#  {it} -> {num}")

        break

    if ":" in text:
        spl = text.split(":")
        course = spl[0]
        password = spl[1]

        first_sort[course] = password

    if "=>" in text:
        spli = text.split("=>")
        courses = spli[0]
        passwords = spli[1]
        name = spli[2]
        number = int(spli[3])
        if courses in first_sort.keys():
            if passwords in first_sort[courses]:
                if name not in second_sort:
                    second_sort[name] = {courses: number}

                else:
                    if courses not in second_sort[name]:
                        second_sort[name].update({courses: number})

                    else:
                        for k, v in second_sort[name].items():
                            if k == courses and v < number:
                                second_sort[name].update({courses: number})


        else:
            text = input()
            continue
    text = input()
