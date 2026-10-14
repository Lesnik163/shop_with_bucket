class Cart:
  def __init__(self):
    self.items = []

  def add_from_catalog(self, catalog, index):
    product = catalog.products[index]
    self.items.append(product)

  def remove_product(self, index):
    self.items.pop(index)

  def show(self):
    print("В корзине:")

    for index, product in enumerate(self.items, start=1):
      print(f"{'-'*40}")
      print(f"{index}.", product.name, product.price, product.weight, product.category)
      print(f"{'-'*40}")

  def total_price(self):
    result = 0
    for product in self.items:
      result += product.price
    return result

  def show_total(self):
    print(f"Сумма: {self.total_price()}\n")

  def remove_same(self, product):
    self.items = [item for item in self.items if item is not product]