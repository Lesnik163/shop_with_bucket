from tkinter.constants import NUMERIC
from catalog import Catalog
from product import Product
from cart import Cart
from sort import sort_items

basket = Cart()


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

def main():
  shop = Catalog()
  while True:
    print("1. Показать каталог")
    print("2. Добавить продукт")
    print("3. Добавить в корзину")
    print("4. Показать корзину")
    print("5. Удалить из корзины")
    print("6. Сумма корзины")
    print("7. Сортировать корзину")
    print("8. Изменить товар в каталоге")
    print("9. Удалить товар из каталога")
    print("10. Выход\n")
    command = input("\nВыберите команду:")
    if command == "1":
      shop.show()
    elif command == "2":
      add_product(shop)
    elif command == "3":
      add_to_cart(shop, basket)
    elif command == "4":
      show_cart(basket)
    elif command == "5":
      remove_from_cart(basket)
    elif command == "6":
      basket.show_total()
    elif command == "7":
      sort_cart(basket)
    elif command == "8":
      edit_in_catalog(shop)
    elif command == "9":
      remove_from_catalog(shop, basket)
    elif command == "10":
      break
    else:
      print("Неверная команда")


if __name__ == "__main__":
  main()