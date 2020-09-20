journey_cost = float(input())  # колко ще струва пътуването
number_of_months = int(input())  # месеци, за които трябва да съберете парите

total = 0
for i in range(1, number_of_months + 1):

    if i > 1:
        if i % 2 != 0:
            total = total - (0.16 * total)  # Изразходваме 16% от събраните пари до момента

    if i % 4 == 0:
        total += 0.25 * total   # Спестяваме 25% от цената на пътуването

    total += 0.25 * journey_cost

if total >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {total - journey_cost:.2f}lv. for souvenirs.")

else:
    print(f"Sorry. You need {journey_cost - total:.2f}lv. more.")
