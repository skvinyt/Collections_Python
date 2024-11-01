import random
import string

# Принимаем длину пароля от пользователя
password_length = int(input("Введите длину пароля: "))

# Определяем набор символов для пароля
characters = string.ascii_letters + string.digits + string.punctuation

# Генерируем случайный пароль
password = ''.join(random.choice(characters) for _ in range(password_length))

# Выводим сгенерированный пароль
print("Сгенерированный пароль:", password)
