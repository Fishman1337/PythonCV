#Inheritance#
#Simple inheritance pet to cat & dog.
class Pet:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def talk(self):
		raise NotImplementedError("Subclass must implement abstract method.")

class Cat(Pet):

	def __init__(self, name, age):
		Pet.__init__ (self, name, age)

	def talk(self):
		return "Meeooow"

class Dog(Pet):

	def __init__(self, name, age):
		Pet.__init__(self, name, age)

	def talk(self):
		return "Woooof!"
#Polymorphism redefining methods with overrides
class Person():

	def payBill():
		raise NotImplementedError

class Millionaire(Person):
	
	def payBill():
		print "Here you are! Keep the change!"

class GradStudent(Person):

	def payBill():
		print "Can I owe you £15?"
#Create two lists of objects % cycle through to demonstrate
def main():

	pets = [Cat("jess", 3), Dog("Jack", 2), Cat("Fred", 7), Pet("thePet", 5)]
	people = [MIllionaire(), GradStudent()]

	for person in people:
		people.payBill()

	for pet in pets:
		print "Name:" + pet.name + ", Age:" + str(pet.age) + ", says:" + pet.talk()

if __name__ == "__main__":
	main()