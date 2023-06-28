def solution(A):
    if len(A) == 0:
        return 0
    minprice = A[0]
    maxprofit = 0
    s = 0
    for i in range(1, len(A)):
        if A[i] < minprice:
            minprice = A[i]
            s = 0
        else:
            s += A[i] - A[i-1]
        if maxprofit < s:
            maxprofit = s
    return maxprofit


A = [23171, 21011, 21123, 21366, 21013, 21367]
print(solution(A))
