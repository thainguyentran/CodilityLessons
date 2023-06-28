def solution(A, B):
    n = len(A)
    downstream = []
    eaten = 0
    for i in range(n):
        if B[i] == 1:
            downstream.append(A[i])
        else:
            while downstream:
                if A[i] > downstream[-1]:
                    downstream.pop(-1)
                    eaten += 1
                else:
                    eaten += 1
                    break
    return n - eaten

A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

print(solution(A, B))
