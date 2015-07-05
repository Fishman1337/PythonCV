def shape(A):
	num_rows = len(A)
	num_cols = len(A[0]) if A else 0 #Number of elements in the first row
	return num_rows, num_cols

def get_column(A, j):
	return [A_i[j]
		forA_i in A]