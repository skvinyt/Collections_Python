# Принимаем два слова от пользователя
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# Проверяем, равна ли длина двух слов
if len(word1) != len(word2):
    print("Слова не являются анаграммами.")
else:
    # Создаем два пустых словаря для хранения частоты символов
    char_count1 = {}
    char_count2 = {}

    # Проход по каждому символу в первом слове и увеличиваем счётчик в словаре
    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    # Проход по каждому символу во втором слове и увеличиваем счётчик в словаре
    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Сравниваем оба словаря
    if char_count1 == char_count2:
        print("Слова являются анаграммами.")
    else:
        print("Слова не являются анаграммами.")
