from matplotlib import pyplot as plt

#GDP line chart
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 545.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.show()

#Oscars bar chart
movies = ["Annie Hall", "Ben Hur", "Casablanca", "Ghandi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)

plt.title("Movies")

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()


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