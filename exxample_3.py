# Входная строка
input_string = input("Введите строку: ")

# Преобразуем все символы в нижний регистр
input_string = input_string.lower()

# Создаем пустое множество для хранения символов, которые встречаются нечетное количество раз
odd_chars = set()

# Проходим по каждому символу в строке
for char in input_string:
    if char in odd_chars:
        odd_chars.remove(char)
    else:
        odd_chars.add(char)

# Определяем размер множества
if len(odd_chars) <= 1:
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
