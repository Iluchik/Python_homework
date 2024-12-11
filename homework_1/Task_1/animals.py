class Animals():

	def __init__(self, name:str, sound:str):
		self.name = name
		self.sound = sound

	def makesound(self):
		print(self.sound)

class Cat(Animals):

	def __init__(self, name: str, sound: str, color: str):
		super().__init__(name, sound)
		self.color = color

	def makesound(self):
		print("Meow!")

class Dog(Animals):

	def __init__(self, name: str, sound: str, color: str):
		super().__init__(name, sound)
		self.color = color

	def makesound(self):
		print("Woof!")

cat = Cat("Ivan", "meow", "grey")
dog = Dog("Petr", "woof", "brown")

cat.makesound()
dog.makesound()