from product import Product
from sort import sort_items


def add_product(shop):
  name = input("Введите название товара: ")
  price = float(input("Введите цену товара: "))
  weight = float(input("Введите вес товара: "))
  category = input("Введите категорию товара: ")
  description = input("Введите описание товара: ")
  product = Product(name, category, price, weight, description)
  shop.add_product(product)

def add_to_cart(shop, basket):
  shop.show()
  if len(shop.products) == 0:
    return
  number = int(input("\nВведите номер товара: "))
  if number < 1 or number > len(shop.products):
    print("Нет товара с таким номером")
    return
  basket.add_from_catalog(shop, number - 1)

def show_cart(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return

  basket.show()

def remove_from_cart(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return
  basket.show()
  number = int(input("\nВведите номер товара в корзине: "))
  if number < 1 or number > len(basket.items):
    print("Нет товара с таким номером в корзине\n")
    return
  basket.remove_product(number - 1)

def sort_cart(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return

  print("1. Пузырёк")
  print("2. Вставки")
  print("3. Быстрая")
  print("4. Слияние")
  choice = input("Алгоритм: ")
  if choice == "1":
    algorithm = "bubble"
  elif choice == "2":
    algorithm = "insertion"
  elif choice == "3":
    algorithm = "quick"
  elif choice == "4":
    algorithm = "merge"
  else:
    print("Нет такого алгоритма\n")
    return

  print("1. Цена")
  print("2. Вес")
  print("3. Категория")
  choice = input("Поле: ")
  if choice == "1":
    field = "price"
  elif choice == "2":
    field = "weight"
  elif choice == "3":
    field = "category"
  else:
    print("Нет такого поля\n")
    return

  print("1. По возрастанию")
  print("2. По убыванию")
  choice = input("Порядок: ")
  if choice == "1":
    descending = False
  elif choice == "2":
    descending = True
  else:
    print("Нет такого порядка\n")
    return

  basket.items = sort_items(basket.items, algorithm, field, descending)
  basket.show()

def edit_in_catalog(shop):
  shop.show()
  if len(shop.products) == 0:
    return
  number = int(input("Номер товара: "))
  if number < 1 or number > len(shop.products):
    print("Нет товара с таким номером\n")
    return
  name = input("Название: ")
  category = input("Категория: ")
  price = float(input("Цена: "))
  weight = float(input("Вес: "))
  description = input("Описание: ")
  shop.edit_product(
    number - 1,
    Product(name, category, price, weight, description)
  )

def remove_from_catalog(shop, basket):
  shop.show()
  if len(shop.products) == 0:
    return
  number = int(input("Номер товара: "))
  if number < 1 or number > len(shop.products):
    print("Нет товара с таким номером\n")
    return
  product = shop.products[number - 1]
  shop.remove_product(number - 1)
  basket.remove_same(product)

def show_discount(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return
  percent = float(input("Введите процент скидки: "))
  if percent < 0 or percent > 100:
    print("Скидка должна быть от 0 до 100\n")
    return
  print(f"Сумма: {basket.total_price()}")
  print(f"Сумма с учетом скидки: {basket.price_with_discount(percent)}\n")

def show_tax(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return
  discount = float(input("Скидка в процентах: "))
  tax = float(input("Налог в процентах: "))
  if discount < 0 or discount > 100 or tax < 0:
    print("Скидка от 0 до 100, налог от 0\n")
    return
  print(f"Сумма: {basket.total_price()}")
  print(f"После скидки: {basket.price_with_discount(discount)}")
  print(f"С налогом: {basket.price_with_tax(discount, tax)}\n")
