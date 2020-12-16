
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def change_email(self):
        self.email = self.name + '@company.com'


person = Person('Ivan', 'ivan@outlook.com')
print(person.email)  # ivan@outlook.com
person.change_email()  # Ivan@company.com
print(person.email)  # Ivan@company.com



# class Person:
#     pass
#
#
# person = {
#     'name': 'Emilian Stoyanov',
#     'email': 'emilianstoyanov@outlook.com'
# }
#
#
# def change_email(person: dict):
#     person['email'] = person['name'] + '@company.com'
#
#
# print(person)
# change_email(person)
# print(person)
# логика за смяна на мейла на пторебител
# когатоизвикаме change_email, и извикаме после person, мейла е сменен
