class Catalog:
  def __init__(self):
    self.products = []

  def add_product(self, product):
    self.products.append(product)

  def edit_product(self, index, product):
    current = self.products[index]
    current.name = product.name
    current.category = product.category
    current.price = product.price
    current.weight = product.weight
    current.description = product.description

  def remove_product(self, index):
    self.products.pop(index)

  def show(self):
    if len(self.products) == 0:
      print("Каталог пуст\n")
      return
    print("В каталоге:\n")
    for index, product in enumerate(self.products, start=1):
      print(
        f"{'-'*40}\n"
        f"{index}. {product.name} - {product.price} - "
        f"{product.weight} - {product.category} - {product.description}\n"
        f"{'-'*40}\n"
      )