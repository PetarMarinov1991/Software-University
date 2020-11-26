from project.software.software import Software


class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value not in {'Heavy', 'Power'}:
            return
        self._type = value

    def install(self, software: Software):
        memory_used = sum([s.memory_consumption for s in self.software_components])
        capacity_used = sum([s.capacity_consumption for s in self.software_components])
        if memory_used + software.memory_consumption <= self.memory \
                or capacity_used + software.capacity_consumption <= self.capacity:
            self.software_components.append(software)
            return
        raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
