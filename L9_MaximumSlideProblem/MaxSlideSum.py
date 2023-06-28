#Kadane algorithm

def solution(A):
    maxsum = A[0]
    s = 0
    for i in range(len(A)):
        s += A[i]
        if A[i] > s:
            s = A[i]
        maxsum = max(s, maxsum)
    return maxsum

A = [3, 2, -6, 4, 0]
# A = [-2, 1]
print(solution(A))
