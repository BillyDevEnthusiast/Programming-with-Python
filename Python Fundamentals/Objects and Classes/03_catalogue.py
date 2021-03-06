class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        res = [product for product in self.products if product.startswith(first_letter)]
        return res

    def __repr__(self):
        res = f"Items in the {self.name} catalogue:\n"
        res += "\n".join(sorted(self.products))
        return res
