from catalog import Catalog
from cart import Cart
from menu import (
  add_product,
  add_to_cart,
  show_cart,
  remove_from_cart,
  sort_cart,
  edit_in_catalog,
  remove_from_catalog,
  show_discount,
  show_tax,
)


def main():
  shop = Catalog()
  basket = Cart()
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
    print("10. Сумма со скидкой")
    print("11. Сумма со скидкой и налогом")
    print("12. Выход\n")
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
      show_discount(basket)
    elif command == "11":
      show_tax(basket)
    elif command == "12":
      break
    else:
      print("Неверная команда")


if __name__ == "__main__":
  main()