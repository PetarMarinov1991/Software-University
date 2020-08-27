class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):
        return f'Items in the {self.name} catalogue:\n' + '\n'.join([product for product in sorted(self.products)])
