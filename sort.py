# Сравнительная таблица
# Алгоритм	  Лучший	    Средний	  Худший	   Память	Стабильная
# Bubble	     O(n)	       O(n²)	   O(n²)	    O(1)	     ✅
# Insertion	   O(n)	       O(n²)	   O(n²)	    O(1)	     ✅
# Quick	    O(n log n)	 O(n log n)	 O(n²)	  O(log n)	   ❌
# Merge	    O(n log n)	 O(n log n)	O(n log n)	O(n)	     ✅

def product_value(product, field):
  if field == "price":
    return product.price
  if field == "weight":
    return product.weight
  if field == "category":
    return product.category
  raise ValueError("неизвестное поле")

def should_swap(left, right, field, descending):
  left_value = product_value(left, field)
  right_value = product_value(right, field)
  if descending:
    return left_value < right_value
  return left_value > right_value


# Чем больше увеличиваем i, тем меньше пар остается для сравнения
# выталкиваем наибольший элемент в конец списка, в конце 
# сравниваем пару (0, 1)
# Для [2, 3, 5, 1] это так:
# i = 0: пары (0, 1), (1, 2), (2, 3) — весь список
# i = 1: пары (0, 1), (1, 2) — правый конец уже не трогаем
# i = 2: пара (0, 1) — слева осталось только два товара
# Время: всегда O(n²). Проходы идут все, даже если список уже отсортирован.
# В таблице лучший случай O(n) — это остановка после прохода без обменов. Здесь её нет.
# Память: O(1), товары меняются местами в том же списке.

def bubble_sort(items, field ='price', descending = False ):
  n = len(items)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if should_swap(items[j], items[j + 1], field, descending):
        items[j], items[j + 1] = items[j + 1], items[j]
  return items

# Сортировка вставками
# Сначала сортируем первые два элемента, затем добавляем третий и т.д.
# Для [2, 3, 5, 1] это так:
# На шаге i = 3 список ещё [2, 3, 5, 1]. Единица не меняется с пятёркой одним обменом. Она сначала запоминается в current, а пятёрка, тройка и двойка по очереди копируются на одну клетку вправо. Единица записывается обратно только когда сдвиги заканчиваются.
# current = 1, j = 2.
# j = 2, в списке 5. 5 > 1, поэтому в клетку 3 копируется 5. Получается [2, 3, 5, 5]. Старая единица уже не в списке, она лежит в current. j становится 1.
# j = 1, в списке 3. 3 > 1, в клетку 2 копируется 3. Получается [2, 3, 3, 5]. j становится 0.
# j = 0, в списке 2. 2 > 1, в клетку 1 копируется 2. Получается [2, 2, 3, 5]. j становится -1.
# Слева клеток больше нет, цикл останавливается. current записывается в клетку 0. Получается [1, 2, 3, 5].
# Время: лучший O(n), средний и худший O(n²). На готовом списке внутренний цикл сразу останавливается.
# Память: O(1), сдвиги идут в том же списке.

def insertion_sort(items, field="price", descending=False):
  for i in range(1, len(items)):
    current = items[i]
    j = i - 1
    while j >= 0 and should_swap(items[j], current, field, descending):
      items[j + 1] = items[j]
      j -= 1
    items[j + 1] = current
  return items

# Быстрая сортировка
# Сначала выбираем опорный элемент (pivot), затем разбиваем список на три части: меньше опорного, равные опорному, больше опорного.
# Для [2, 3, 5, 1] это так:
# pivot = 5
# left = [2, 3, 1]
# middle = [5]
# right = []
# Время: лучший и средний O(n log n), худший O(n²), если опора каждый раз почти не делит список.
# Память: O(n). left, middle и right — новые списки.
# В таблице O(log n) — память быстрой сортировки на месте, только под вложенные вызовы.

def quick_sort(items, field="price", descending=False):
  if len(items) <= 1:
    return items
  pivot = items[len(items) // 2]
  left = [x for x in items if should_swap(pivot, x, field, descending)]
  middle = [x for x in items if product_value(x, field) == product_value(pivot, field)]
  right = [x for x in items if should_swap(x, pivot, field, descending)]
  return quick_sort(left, field, descending) + middle + quick_sort(right, field, descending)

# Сортировка слиянием
# Сначала делим список пополам, затем сортируем каждую половину,
# если длина половинок больше 1, то делим пополам и сортируем,
# затем сливаем результаты.
# Для [2, 3, 5, 1] это так:
# mid = 2
# left = [2, 3] -> [2], [3]
# right = [5, 1] -> [5], [1]
# left = [2], right = [3] -> [2, 3]
# left = [5], right = [1] -> [1, 5]
# [2, 3] и [1, 5] -> [1, 2, 3, 5]
# Время: всегда O(n log n).
# Память: O(n), половины и слитый результат лежат в новых списках.

def merge_sort(items, field="price", descending=False):
  if len(items) <= 1:
    return items
  mid = len(items) // 2
  left = items[:mid]
  right = items[mid:]
  sorted_left = merge_sort(left, field, descending)
  sorted_right = merge_sort(right, field, descending)
  return merge(sorted_left, sorted_right, field, descending)
def merge(left, right, field="price", descending=False):
  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if not should_swap(left[i], right[j], field, descending):
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result

def sort_items(items, algorithm, field="price", descending=False):
  if algorithm == "bubble":
    return bubble_sort(items, field, descending)
  if algorithm == "insertion":
    return insertion_sort(items, field, descending)
  if algorithm == "quick":
    return quick_sort(items, field, descending)
  if algorithm == "merge":
    return merge_sort(items, field, descending)
  raise ValueError("неизвестный алгоритм")