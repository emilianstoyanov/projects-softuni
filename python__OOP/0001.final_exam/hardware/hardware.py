from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        occupied_memory = sum([s.memory_consumption for s in self.software_components])
        occupied_capacity = sum([s.capacity_consumption for s in self.software_components])
        if software.capacity_consumption + occupied_capacity > self.capacity \
                or software.memory_consumption + occupied_memory > self.memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
