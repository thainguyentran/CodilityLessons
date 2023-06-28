def solution(A):
    A.sort()
    end = len(A)-1
    while end >= 2:
        if A[end-2] + A[end-1] > A[end]:
            return 1
        else:
            end -= 1
    return 0
A=[5, 3, 3]
print(solution(A))
