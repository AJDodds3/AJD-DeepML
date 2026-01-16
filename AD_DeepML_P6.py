import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues = []
	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	desc = math.sqrt(trace**2 - 4*det)
	eigenvalues.append((trace + desc) / 2)
	eigenvalues.append((trace - desc) / 2)
	return sorted(eigenvalues, reverse=True)