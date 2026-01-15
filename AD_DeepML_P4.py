def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	total = 0
	counter = 0
	if mode == "row":
		for i in range(len(matrix)):
			total = 0
			counter = 0
			for j in range(len(matrix[0])):
				total += matrix[i][j]
				counter += 1
			means.append(total/counter)
	else:
		for i in range(len(matrix[0])):
			total = 0
			counter = 0
			for j in range(len(matrix)):
				total += matrix[j][i]
				counter += 1
			means.append(total/counter)

	return means