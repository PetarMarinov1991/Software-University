from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_name = [h for h in System._hardware if h.name == hardware_name]
        if not hardware_name:
            return 'Hardware does not exist'
        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware_name[0].install(new_software)
            System._software.append(new_software)
        except:
            return 'Software cannot be installed'

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_name = [h for h in System._hardware if h.name == hardware_name]
        if not hardware_name:
            return 'Hardware does not exist'
        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware_name[0].install(new_software)
            System._software.append(new_software)
        except:
            return f'Software cannot be installed'

    @staticmethod
    def release_software_component(hardware_name, software_name):
        current_hardware = [h for h in System._hardware if h.name == hardware_name]
        current_software = [s for s in System._software if s.name == software_name]
        if not (current_hardware and current_software):
            return 'Some of the components do not exist'
        current_hardware[0].uninstall(current_software[0])
        System._software.remove(current_software[0])

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        used_memory = [sum([s.memory_consumption for s in h.software_components]) for h in System._hardware][0]
        used_capacity = [sum([s.capacity_consumption for s in h.software_components]) for h in System._hardware][0]
        return f'System Analysis\n' \
               f'Hardware Components: {len(System._hardware)}\n' \
               f'Software Components: {len(System._software)}\n' \
               f'Total Operational Memory: {used_memory} / {total_memory}\n' \
               f'Total Capacity Taken: {used_capacity} / {total_capacity}'

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            name = h.name
            length_express = len([s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"])
            length_light = len([s for s in h.software_components if s.__class__.__name__ == "LightSoftware"])
            memory_usage = sum([s.memory_consumption for s in h.software_components])
            capacity_usage = sum([s.capacity_consumption for s in h.software_components])
            software_components = ', '.join(s.name for s in h.software_components)
            result += f'Hardware Component - {name}\n' \
                      f'Express Software Components: {length_express}\n' \
                      f'Light Software Components: {length_light}\n' \
                      f'Memory Usage: {memory_usage} / {h.memory}\n' \
                      f'Capacity Usage: {capacity_usage} / {h.capacity}\n' \
                      f'Type: {h.type}\n' \
                      f'Software Components: {software_components}'
        return result
