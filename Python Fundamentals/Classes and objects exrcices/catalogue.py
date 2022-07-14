class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.reduced_products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)
        return self.products

    def get_by_letter(self, first_letter: str):
        for i in self.products:
            if i[0] == first_letter:
                self.reduced_products.append(i)

        return self.reduced_products

    def __repr__(self):
        self.products.sort()
        x = '\n'
        return f"Items in the {self.name} catalogue:\n{x.join(self.products)}"




catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
