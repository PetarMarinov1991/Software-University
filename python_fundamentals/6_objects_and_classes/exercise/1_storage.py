class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if self.capacity > 0:
            self.storage.append(product)
            self.capacity -= 1

    @staticmethod
    def get_products():
        return Storage.storage
