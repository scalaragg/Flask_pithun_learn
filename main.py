# 1. Создать list из 10 чисел.


numbers = list(range(1, 11))
even_numbers = [number for number in numbers if number % 2 == 0]

print("Чётные числа:", even_numbers)


# 2. Создать dict «товар → цена».


products = {
    "хлеб": 50,
    "молоко": 80,
    "сыр": 300
}

products["молоко"] = 90

print("\nТовары и цены:")
for product, price in products.items():
    print(f"{product}: {price} руб.")


# 3. Создать set из списка с дублями.


numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = set(numbers_with_duplicates)

print("\nSet без дубликатов:", unique_numbers)

print("Есть ли число 3?", 3 in unique_numbers)


# 4. Создать tuple координат.


point = (10, 20)

print("\nКоординаты:", point)

try:
    point[0] = 100
except TypeError as error:
    print("Ошибка:", error)


# 5. Сравнить обычный цикл for и comprehension.


numbers = [1, 2, 3, 4, 5]

squares_for = []

for number in numbers:
    squares_for.append(number ** 2)

squares_comprehension = [number ** 2 for number in numbers]

print("\nКвадраты через for:", squares_for)
print("Квадраты через comprehension:", squares_comprehension)


# Проверка

assert isinstance(numbers, list)
assert isinstance(products, dict)
assert isinstance(unique_numbers, set)
assert isinstance(point, tuple)
