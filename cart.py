class Cart:
  def __init__(self):
    self.items = []

  def add_from_catalog(self, catalog, index):
    product = catalog.products[index]
    self.items.append(product)

  def remove_product(self, index):
    self.items.pop(index)

  def show(self):
    for index, product in enumerate(self.items):
      print(index, product.name, product.price, product.weight, product.category)

  def total_price(self):
    result = 0
    for product in self.items:
      result += product.price
    return result