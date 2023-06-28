def solution(A):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    count = 1
    B = A.copy()
    B.sort()
    for i in range(len(B)):
        if B[i] != B[i-1]:
            count = 1
        else:
            count += 1
        if count > len(B)//2:
            return A.index(B[i])
    return -1


#A = [3, 4, 3, 2, 3, -1, 3, 3]
A = [2,1,4,7,4,8,3,6,4,7]
print(solution(A))
