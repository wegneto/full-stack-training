class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last name: " + self.last_name)
		print("Eye color: " + self.eye_color)

class Child(Parent):
		def __init__(self, last_name, eye_color, number_of_toys):
			print("Child constructor called")
			Parent.__init__(self, last_name, eye_color)
			self.number_of_toys = number_of_toys

		def show_info(self):
			print("Last name: " + self.last_name)
			print("Eye color: " + self.eye_color)
			print("Number of toys: " + str(self.number_of_toys))

john_doe = Parent("Doe", "brown")
#john_doe.show_info()

jane_doe = Child("Doe", "brown", 5)
jane_doe.show_info()