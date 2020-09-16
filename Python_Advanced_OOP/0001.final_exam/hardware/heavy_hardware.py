from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name: str,  capacity: int, memory):
        Hardware.__init__(self, name, "Heavy", capacity * 2, memory * 0.75)
