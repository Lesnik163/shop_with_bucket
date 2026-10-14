from product import Product
from sort import sort_items


def read_float(prompt, minimum=None, maximum=None):
  while True:
    try:
      value = float(input(prompt))
    except ValueError:
      print("Введите число")
      continue
    if minimum is not None and value < minimum:
      print(f"Число должно быть не меньше {minimum}")
      continue
    if maximum is not None and value > maximum:
      print(f"Число должно быть не больше {maximum}")
      continue
    return value

def read_int(prompt, minimum, maximum):
  while True:
    try:
      value = int(input(prompt))
    except ValueError:
      print("Введите целое число")
      continue
    if value < minimum or value > maximum:
      print(f"Введите номер от {minimum} до {maximum}")
      continue
    return value

def read_choice(prompt, choices):
  while True:
    choice = input(prompt)
    if choice in choices:
      return choice
    print("Нет такого варианта")

def add_product(shop):
  name = input("Введите название товара: ")
  price = read_float("Введите цену товара: ", minimum=0)
  weight = read_float("Введите вес товара: ", minimum=0)
  category = input("Введите категорию товара: ")
  description = input("Введите описание товара: ")
  product = Product(name, category, price, weight, description)
  shop.add_product(product)

def add_to_cart(shop, basket):
  shop.show()
  if len(shop.products) == 0:
    return
  number = read_int(
    "\nВведите номер товара: ", 1, len(shop.products)
  )
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
  number = read_int(
    "\nВведите номер товара в корзине: ", 1, len(basket.items)
  )
  basket.remove_product(number - 1)

def sort_cart(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return

  print("1. Пузырёк")
  print("2. Вставки")
  print("3. Быстрая")
  print("4. Слияние")
  choice = read_choice("Алгоритм: ", {"1", "2", "3", "4"})
  algorithms = {
    "1": "bubble",
    "2": "insertion",
    "3": "quick",
    "4": "merge",
  }
  algorithm = algorithms[choice]

  print("1. Цена")
  print("2. Вес")
  print("3. Категория")
  choice = read_choice("Поле: ", {"1", "2", "3"})
  fields = {
    "1": "price",
    "2": "weight",
    "3": "category",
  }
  field = fields[choice]

  print("1. По возрастанию")
  print("2. По убыванию")
  choice = read_choice("Порядок: ", {"1", "2"})
  descending = choice == "2"

  print("1. Показать шаги")
  print("2. Без шагов")
  choice = read_choice("Шаги: ", {"1", "2"})
  show_steps = choice == "1"

  basket.items = sort_items(basket.items, algorithm, field, descending, show_steps)
  basket.show()

def edit_in_catalog(shop):
  shop.show()
  if len(shop.products) == 0:
    return
  number = read_int("Номер товара: ", 1, len(shop.products))
  name = input("Название: ")
  category = input("Категория: ")
  price = read_float("Цена: ", minimum=0)
  weight = read_float("Вес: ", minimum=0)
  description = input("Описание: ")
  shop.edit_product(
    number - 1,
    Product(name, category, price, weight, description)
  )

def remove_from_catalog(shop, basket):
  shop.show()
  if len(shop.products) == 0:
    return
  number = read_int("Номер товара: ", 1, len(shop.products))
  product = shop.products[number - 1]
  shop.remove_product(number - 1)
  basket.remove_same(product)

def show_discount(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return
  percent = read_float(
    "Введите процент скидки: ", minimum=0, maximum=100
  )
  print(f"Сумма: {basket.total_price()}")
  print(f"Сумма с учетом скидки: {basket.price_with_discount(percent)}\n")

def show_tax(basket):
  if len(basket.items) == 0:
    print("Корзина пуста\n")
    return
  discount = read_float(
    "Скидка в процентах: ", minimum=0, maximum=100
  )
  tax = read_float("Налог в процентах: ", minimum=0)
  print(f"Сумма: {basket.total_price()}")
  print(f"После скидки: {basket.price_with_discount(discount)}")
  print(f"С налогом: {basket.price_with_tax(discount, tax)}\n")
