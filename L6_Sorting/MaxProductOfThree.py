
def solution(A):
    A.sort()
    size = len(A)
    result = max(A[0] * A[1] * A[size - 1],  A[size - 1] * A[size - 2] * A[size - 3])
    return result


A = [-5, 5, -5, 4]
print(solution(A))
