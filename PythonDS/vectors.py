import math
#Vectors
height_weight_age = [70, 170, 40]

grades = [95, 80, 75, 62]

def vector_add(v, w):
	#Add elements
	return [v_i + w_i
		for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
	#Subtract corresponding elements
	return[v_i - w_i
		for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
	#Sum all corresponding elements
	return reduce(vector_add, vectors)
	"""
	returl = vectors[0]
	for vector in vectors[1:]:
		result = vector_add(result, vector)
	return result
	"""

def scalar_multiply(c, v):
	#C number, V vector
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	#Commute the vector whos ith element is the mean of the
	#ith elements of the input vectors
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
	#v_1 * w_1 + ... + v_n * w_n
	return sum(v_i * w_i
		for v_i, w_i in zip(v, w))

def sum_of_squares(v):
	return dot(v, v)

def magnitude(v):
	return math.sqrt(sum_of_squares(v))

def squares_distance(v, w):
	#(v_1 - w_1) ** 2 + ... + (v_n - w_n ** 2)
	return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
	return magnitude(vector_subtract(v, w))

