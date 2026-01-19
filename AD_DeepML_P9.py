import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m, n = len(a), len(a[0])
    o, p = len(b), len(b[0])

    if (n == o):
        a = np.array(a)
        b = np.array(b)
        c = a @ b
        return c
    else:
        return -1     