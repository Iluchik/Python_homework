class Buffer():
	memory: list

	def __init__(self):
		self.memory = []

	def add_data(self, data):
		if len(self.memory) >= 5:
			self.memory.clear()
			print("Переполнение буфера! Очистка буфера...")
			return
		self.memory.append(data)
		print("Данные успешно сохранены!")
		return
	
	def get_data(self):
		if self.memory == []:
			return print("Буфер пуст!")
		return print(self.memory)
	
buffer = Buffer()

if __name__ == "__main__":
	try:
		while True:
			print("Вызовите одну из функций: add_data() или get_data()")
			line = input()
			if line == "add_data()":
				print("Введите значение:", end=" ")
				value = input()
				buffer.add_data(value)
			elif line == "get_data()":
				buffer.get_data()
			else:
				continue
	except KeyboardInterrupt:
		pass