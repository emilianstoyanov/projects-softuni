class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __add__(self, other):
        name = self.name
        surname = other.surname
        return Person(name, surname)
 
 
    def __str__(self):
        return f"{self.name} {self.surname}"
 
 
class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people
 
    def __add__(self, other):
        return Group(self.name, self.people + other.people)
 
    def __len__(self):
        return len(self.people)
 
    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"
 
    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"
