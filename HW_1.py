from datetime import datetime

def get_days_from_today(date):
    
    # Отримання поточної дати
    current_date = datetime.now().date()

    # Перетворення рядка з датою на об'єкт datetime
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError as e:
        print(f"Помилка формату дати: {e}. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'.")
        return None

    # Обчислення різниці між датами
    delta = current_date - given_date

    # Повернення абсолютного значення кількості днів
    return (delta.days)

# Приклади використання функції
print(get_days_from_today('2020-10-09'))
print(get_days_from_today('20-10-09'))
print(get_days_from_today('2025-10-25'))

import random

def get_numbers_ticket(min, max, quantity):
     # 1. Перевірка параметрів на відповідність заданим обмеженням
    # Діапазон чисел від 1 до 1000 включно
    if not (1 <= min <= max <= 1000):
        return []
    # Кількість чисел має бути в межах доступного діапазону
    if not (1 <= quantity <= (max - min + 1)):
        return []

    # 2. Генерація унікальних випадкових чисел
    # random.sample() повертає список унікальних елементів
    # з вказаного діапазону (range) у кількості quantity
    try:
        random_numbers = random.sample(range(min, max + 1), quantity)
    except ValueError:
        # Обробка помилки, якщо quantity більше ніж доступний діапазон,
        return []

    # 3. Сортування та повернення результату
    random_numbers.sort()
    return random_numbers


lottery_numbers_1 = get_numbers_ticket(1, 1000, 9)
print(f"Ваші лотерейні номери: {lottery_numbers_1}") 

lottery_numbers_2 = get_numbers_ticket(1, 2000, 9)
print(f"Ваші лотерейні номери: {lottery_numbers_2}")


import re

def normalize_phone(phone_number):
   # Видаляємо всі символи, крім цифр і '+'
    # Спочатку зберігаємо '+', якщо він є на початку
    if phone_number.strip().startswith('+'):
        cleaned_number = '+' + ''.join(filter(str.isdigit, phone_number))
    else:
        cleaned_number = ''.join(filter(str.isdigit, phone_number))

    # Перевіряємо та додаємо міжнародний код, якщо необхідно
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    elif not cleaned_number.startswith('+'):
        return '+38' + cleaned_number
    else:
        return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for number in raw_numbers:
    normalized = normalize_phone(number)
    print(f"Оригінал: {number:<20} | Нормалізований: {normalized}")



