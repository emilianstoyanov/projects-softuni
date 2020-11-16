class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):  # добавя животно
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):  # наем работник
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):  # пожарникар  /  име на работник
        try:
            search_worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(search_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):  # заплати работник
        to_pay = sum([worker.salary for worker in self.workers])
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):  # обслужвани животни
        to_pay = sum([animal.get_needs() for animal in self.animals])
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):  # печалба , количество
        self.__budget += amount

    def animals_status(self):  # състояние на животните
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetah = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([l.__repr__() for l in lions]) + "\n"
        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join([l.__repr__() for l in tigers]) + "\n"
        result += f"----- {len(cheetah)} Cheetahs:\n"
        result += "\n".join([l.__repr__() for l in cheetah])

        return result

    def workers_status(self):
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [k for k in self.workers if k.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([k.__repr__() for k in keepers]) + "\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([c.__repr__() for c in caretakers]) + "\n"
        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join([v.__repr__() for v in vets])

        return result

