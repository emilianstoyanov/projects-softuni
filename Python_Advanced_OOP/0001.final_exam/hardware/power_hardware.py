from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity, memory):
        Hardware.__init__(self, name, "Power", capacity * 0.25, memory * 1.75)
