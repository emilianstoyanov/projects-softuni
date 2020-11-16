
class Software:
    def __init__(self, name: str, type: str, capacity_consumption, memory_consumption):
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    def __repr__(self):
        return self.name

