# file = open('Open_file.py', 'r')
# print(file.read())
#
#
# file = open('Open_file.py', 'r')
# print(file.readline())
#
#
# file = open('Open_file.py', 'r')
# print(file.readlines())
#
#
# file = open('c:/Users/emili/PycharmProjects/mid_exam/1.Dating App.py', 'r')
# print(file.readline())
#
#
# file = open('Open_file.py', 'r')
# print(file.read(2))
# print(file.read(2))
# print(file.read(2))
# print(file.read())
# # чете по две символа


#
# file_path = "./files/to_write.txt"
# file = open(file_path, 'w')
# file.write("Emo")
# # намери файла с това име, изтрии всичко в него, НО ако не съществува, създай го
# # после пишем във файла с file.write("Emo")


# file_path = "./files/to_write.txt"
# file = open(file_path, 'a')
# file.write("EmoAppend")
# # апендва текст към файла


# file_path = "./files/to_write_2.txt"
# file = open(file_path, 'x')
# file.write("Emo")
# # създава файл с това име, после пишем в него, но ако съществува, хвърля грешка

#
# file_path = "./files/to_write_2.txt"
# file = open(file_path, 'a')
# file.writelines("\n new, emo, new")
# file.close()
# # дописваме на реда във зададения файл, на нов ред с "\n"


file_path = "./files/to_write_2.txt"
with open(file_path, "a") as file:
    file.writelines(["\n new, emo2, new"])
# този вариант е същия, като горния, но без да изписвале .close(), не ни се налага
# да се сещаме да го пишем
# изписваме тескта в подадения файл, няма нужда се затваря с тази команда












