from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption: int, memory_consumption: int):
        Software.__init__(self, name, "Express", capacity_consumption, memory_consumption * 2)
