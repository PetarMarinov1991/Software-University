class Equipment:
    auto_incremental_id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.auto_incremental_id
        Equipment.auto_incremental_id += 1

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'

    @staticmethod
    def get_next_id():
        return Equipment.auto_incremental_id
