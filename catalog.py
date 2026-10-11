class Catalog:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def edit_product(self, index, product):
    self.products[index] = product

  def remove_product(self, index):
    self.products.pop(index)