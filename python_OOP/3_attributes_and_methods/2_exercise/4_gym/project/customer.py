class Customer:
    auto_incremental_id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.auto_incremental_id
        Customer.auto_incremental_id += 1

    def __repr__(self):
        info = f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
        return info

    @staticmethod
    def get_next_id():
        return Customer.auto_incremental_id
