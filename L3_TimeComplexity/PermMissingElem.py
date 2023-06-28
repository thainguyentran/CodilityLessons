# PermMissingElem
# 1 to n
# there is a missing element
# find the missing element

def solution(A):
    # Implement your solution here
    n = len(A)+1
    sumofA = (n * (n+1))//2
    actualsumofA = sum(A)
    return sumofA - actualsumofA

A = [2, 3, 1, 5]
print(solution(A))
