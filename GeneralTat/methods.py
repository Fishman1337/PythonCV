#Simple methods practice.
import math

class Vector2D:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	#Addition:
	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	#Subtraction:
	def __sub__(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	#Multiplication:
	def __mul__(self, other):
		return Vector2D(self.x * other.x, self.y * other.y)

	def __imul__(self, other):
		self.x *= other.x
		self.y *= other.y
		return self

	#Division
	def __div__(self, other):
		return(self.x / float(other.x), self.y / float(other.y))

	def __idiv__(self, other):
		self.x /= other.x
		self.y /= other.y
		return self
		
	def getLength(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalised(self):
		length = self.getLength()
		if length != 0:
			return self/Vector2D(length, length)
		return Vector2D(self)

	def getAngle(self):
		return math.degrees(math.atan2(self.x, self.y))

	def __str__(self):
		return "X: " + str(self.x) + ", Y: " + str(self.y)

def main():
	
	vec = Vector2D(5, 6)
	vec2 = Vector2D(2, 3)

	print "Vec: " + vec
	print "Vec2: " + vec2

	tempmethod = vec.getAngle

	vec = vec + vec2
	print vec

	vec += vec2
	print vec

	vec *= Vector2D(2, 2)
	print vec

	print vec.normalised()
	print vec.getAngle()

	print tempmethod()

if __name__ == "__main__":
	main() 