# Входная строка
input_string = "10 20 50 30 40"

# Разделяем строку на отдельные числа и преобразуем их в целые числа
numbers = [int(num) for num in input_string.split()]

# Инициализируем переменную для хранения наибольшего числа
max_number = numbers[0]

# Проходим по каждому элементу списка
for number in numbers:
    # Сравниваем текущий элемент с наибольшим числом
    if number > max_number:
        max_number = number

# Выводим наибольшее число
print(max_number)  # Вывод: 50
