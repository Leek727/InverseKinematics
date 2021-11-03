import numpy as np
A = [(0, 65), (0, 64), (24, 63), (23, 63), (22, 63), (21, 63), (20, 63), (22, 62), (27, 63)]
B = (0,238)

def find_closest(B, A):
    A = np.array(A)
    leftbottom = np.array(B)
    distances = np.linalg.norm(A-leftbottom, axis=1)
    min_index = np.argmin(distances)
    return A[min_index]

if __name__ == "__main__":
    print(find_closest(A, B))