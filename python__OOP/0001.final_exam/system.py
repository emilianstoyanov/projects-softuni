from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    def __init__(self):
        self._hardware = []
        self._software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        current = PowerHardware(name, capacity, memory)
        System._hardware.append(current)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        current = HeavyHardware(name, capacity, memory)
        System._hardware.append(current)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hw = [h for h in System._hardware if h.name == hardware_name]

        if len(hw) < 1:
            return 'Hardware does not exist'
        current_s = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hw[0].install(current_s)
        except Exception as context:
            return f'{context}'

        System._software.append(current_s)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hw = [h for h in System._hardware if h.name == hardware_name]

        if len(hw) < 1:
            return 'Hardware does not exist'
        current_s = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hw[0].install(current_s)
        except Exception as context:
            return f'{context}'
        System._software.append(current_s)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hw = [h for h in System._hardware if h.name == hardware_name]
        sw = [s for s in System._software if s.name == software_name]
        if len(hw) < 1 or len(sw) < 1:
            return 'Some of the components do not exist'
        hw[0].uninstall(sw[0])
        System._software.remove(sw[0])

    @staticmethod
    def analyze():
        result = f'System Analysis\n'
        hw_comp = len(System._hardware)
        sw_comp = len(System._software)
        total_op_m = 0
        total_c_m = 0
        for h in System._hardware:
            total_op_m += h.memory
            total_c_m += h.capacity
        used_op_m = 0
        used_c_m = 0
        for h in System._hardware:
            for s in h.software_components:
                used_op_m += s.memory_consumption
                used_c_m += s.capacity_consumption

        result += f'Hardware Components: {hw_comp}\n'
        result += f'Software Components: {sw_comp}\n'
        result += f'Total Operational Memory: {used_op_m} / {total_op_m}\n'
        result += f'Total Capacity Taken: {used_c_m} / {total_c_m}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += f'{h}\n'
        return result


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
System.release_software_component("SSD", "Linux")

print(System.system_split())
