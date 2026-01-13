def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	else:
		temp = [] # hold the calculation
		for i in range(len(a)):
			total = 0 # store the total for each list element * b at the same column
			for j in range(len(a[i])):
				total += a[i][j] * b[j]
			temp.append(total)
		return temp


