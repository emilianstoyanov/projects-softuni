from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    def __init__(self):
        Medicine.__init__(self, 20)
