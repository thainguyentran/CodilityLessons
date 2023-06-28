
def solution(X, A):
    # Implement your solution here
    values = set()
    for i in range(len(A)):
        if A[i] <= X:
            values.add(A[i])
        if len(values) == X:
            return i
    return -1

A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5

print(solution(X, A))