count = int(input())

total1 = 0
total2 = 0
for i in range(1, count + 1):
    text = input()
    separation = text.split("|")


    left = separation[0].split(">")
    right = separation[-1].split("<")


    if left[0] == right[1] and len(left[0]) == len(right[1]):
        if ">" in separation[0] and "<" in separation[-1]:  # проверка за знаците, дали се съдържат в началото и в края
            if text.count("|") == 3:  # Проверка, дали съдържа 3 броя чертички
                if left[1].isdigit() and separation[1].islower() and separation[2].isupper():
                    serch = right[0].count("<")
                    serch2 = right[0].count(">")
                    if serch2 == 0 and serch2 == 0:

                        final = "".join(separation)
                        cut = int(len(right[1])) + 1
                        print(f"Password: {final[cut:-cut]}")

                    else:
                        print("Try another password!")

                else:
                    print("Try another password!")
            else:
                print("Try another password!")
        else:
            print("Try another password!")
    else:
        print("Try another password!")





# Започва с група символи и завършва със същите символи (една и съща дължина)

# Има повече от знак (>) след първата група и по-малко от знак (<) преди последната

# Между по-големи от знака и по-малко от знак има четири групи (всяка от три знака),
# разделени с тръба ("|")

# - пътвата група са само числа
# втората група са малки букви
# третата група са големи букви
# четвъртата само символи

# При невалидна парола, принт: "Try another password!"