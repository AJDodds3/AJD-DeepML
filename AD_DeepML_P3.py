import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    rows = len(a)
    cols = len(a[0])
    newr = new_shape[0]
    newc = new_shape[1]
    if ((rows * cols) != newr * newc):
        return []
    a = np.array(a)
    a.reshape((new_shape[0], new_shape[1]))
	return a.tolist()