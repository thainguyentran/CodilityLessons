# Check whether array A is a permutation.

def solution(A):
    n = len(A)
    setA = set(A)
    if len(setA) == n:
        sumofAll = (n * (n+1))//2
        sumofA = sum(A)
        if sumofA == sumofAll:
            return 1
        else:
            return 0
    else:
        return 0


A = [1, 4, 1]
print(solution(A))
