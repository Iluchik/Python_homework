from itertools import count, repeat, chain
from time import sleep

# 1. Создание бесконечного генератора чисел.
inf_generator = (x for x in count())
print("Запуск бесконечного генератора...", "Чтобы прервать нажмите Ctrl+C", sep="\n")
try:
	my_list = []
	for i in inf_generator:
		print(i)
		my_list.append(i)
		sleep(0.2)
except KeyboardInterrupt:
	pass

# 2. Применение функций к каждому элементу в итераторе.
my_list=map(pow, my_list, repeat(2)) # repeat(2) - возведение во вторую степень, repeat(3) - в третью, и т.д.
for i in my_list:
	print(i, end=" ")

# 3. Объединение нескольких итераторов в один.
try:
	print("\nВведите первый массив данных в формате: 01234")
	old_list1 = list(input())
	if old_list1 == [] or old_list1 is None:
		raise ValueError
	print(old_list1)
	print("Введите второй массив данных в формате: 01234")
	old_list2 = list(input())
	if old_list2 == [] or old_list2 is None:
		raise ValueError
	print(old_list2)
	print(list(chain(old_list1, old_list2)))
except ValueError as e:
	print(e.with_traceback)
except KeyboardInterrupt:
	pass