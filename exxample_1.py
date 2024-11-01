# Исходный список
input_list = [1, 2, 3, 2, 1, 4, 5, 4, 6]

# Создаем пустой список для хранения дублирующихся элементов
duplicates = []

# Проходим по каждому элементу в исходном списке
for item in input_list:
    # Проверяем, сколько раз элемент встречается в списке
    count = 0
    for element in input_list:
        if element == item:
            count += 1

    # Если элемент встречается более одного раза и еще не добавлен в список дублирующихся элементов
    if count > 1 and item not in duplicates:
        duplicates.append(item)

# Выводим список дублирующихся элементов
print(duplicates)  # Вывод: [1, 2, 4]
