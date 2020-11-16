needed_experience = float(input())  # 500      при достигане на стойността, принтираме броя завъртания
count = int(input())  # 5        брой завъртания
counter = 0
total = 0

for i in range(1, count + 1):
    input_number = float(input())  # входните данни
    total += input_number
    counter += 1

    if i % 3 == 0:
        total += input_number * 0.15  # добавяме 15% повече

    if i % 5 == 0:
        total -= input_number * 0.10  # приспадаме 10 %

    if total >= needed_experience:
        print(f"Player successfully collected his needed experience for {counter} battles.")
        break

else:
    print(f"Player was not able to collect the needed experience, {needed_experience - total:.2f} more needed.")

# Изчислете дали той може да отключи резервоара. Имайте предвид, че той получава 15% повече
# опит за всяка трета битка и 10% по-малко за всяка пета битка. Също така трябва да спрете
# програмата веднага щом той събере нужния опит.

# Ако той е успял да събере опита, отпечатайте колко битки са му били в следния формат:
# Player successfully collected his needed experience for {battleCount} battles.

# Ако той не е в състояние да го направи, отпечатайте следното съобщение:
# Player was not able to collect the needed experience, {neededExperience} more needed.
