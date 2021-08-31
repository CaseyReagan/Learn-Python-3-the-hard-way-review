## Animal is-a object (yes, sort of confusing) look at the extra credit
# object可以不写，但是最好也可以写出来
class Animal(object):
	pass

## Dog is-a Animal and a object
class Dog(Animal):

	def __init__(self, name):
		## Dog has a name
		self.name = name

## Cat is a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has a name
		self.name = name

## Person is a object
class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name
		## Person has a pet of some kind
		self.pet = None

## 
class Employee(Person):
	"""docstring for Employee"""
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has salary
		self.salary = salary

## Fish is a object
class Fish(object):
	pass

## Salmon is a Fish and object
class Salmon(Fish):
	pass

## Halibut is a Fish and object
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has a pet satan
mary.pet = satan

## frank ia-a Enployee with 120000 salary
frank = Employee("Frank",120000)

## frank has a pet rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()