class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
		def __init__(self, last_name, eye_color, number_of_toys):
			print("Child constructor called")
			Parent.__init__(self, last_name, eye_color)
			self.number_of_toys = number_of_toys

john_doe = Parent("Doe", "brown")
print(john_doe.last_name)

jane_doe = Child("Doe", "brown", 5)
print(jane_doe.last_name)
print(jane_doe.number_of_toys)