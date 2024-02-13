import numpy as np

TD = np.array([
    [2, 3, 0, 3, 7],
    [0, 5, 5, 0, 3],
    [5, 0, 7, 3, 3],
    [3, 1, 0, 9, 9],
    [0, 0, 7, 1, 3],
    [6, 9, 4, 6, 0]
])

total_terms = np.sum(TD)

print(total_terms)
