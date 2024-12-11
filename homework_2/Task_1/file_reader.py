from re import search

try:
	with open('data.txt', 'r', encoding='utf-8') as file:
		data = file.readlines()
		for line in data:
			result = search(r"[^0-9\n]", line)
			if result is not None:
				raise TypeError
			else:
				print(line)
		print("Программа успешно завершила свою работу!")
except FileNotFoundError as e:
	print(f"FileNotFoundError: {e.strerror}")
except TypeError as e:
	print(f"TypeError: {e.with_traceback}")