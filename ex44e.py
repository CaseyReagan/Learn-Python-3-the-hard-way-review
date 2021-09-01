## Use composition to do implicit inheritance
## 这两个类没有继承关系，但通过调用，也可以实现类似的功能
class Other(object):

	def override(self):
		print("OTHER override()")

	def implicit(self):
		print("OTHER implicit()")

	def altered(self):
		print("OTHER altered()")

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print("CHILD override()")

	def altered(self):
		print("CHILD, Before OTHER altered()")
		self.other.altered()
		print("CHILD, After OTHER altered()")

son = Child()

son.implicit()

son.override()

son.altered()
