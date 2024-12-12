from datetime import datetime

# 1. Отображение текущей даты и времени.
print(datetime.now())

# 2. Вычисление разницы между двумя датами.
print(datetime.now() - datetime(2024, 12, int(input()))) # Введи число равно дню месяца

# 3. Преобразование строки в объект даты и времени.
input_date = input() # Введи дату и время в формате %d-%B-%Y %H:%M:%S, например 12-12-2024 12:00:01
print(input_date, "->", datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S"))