from project.medicine.medicine import Medicine


class Salve(Medicine):
    def __init__(self):
        Medicine.__init__(self, 50)
