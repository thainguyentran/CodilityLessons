def solution(A):
    #This solution got 55%, those that didnt pass was due to timed out
    # if len(A) <= 1:
    #     return 0
    # countH = 1
    # countT = 1
    #
    # equi_count = 0
    # for s in range(1, len(A)):
    #     H = A[0:s]
    #     T = A[s:len(A)]
    #     leaderH = -1
    #     leaderT = -999
    #     if s > 1:
    #         H.sort()
    #         for i in range(len(H)):
    #             if H[i] != H[i - 1]:
    #                 countH = 1
    #             else:
    #                 countH += 1
    #             if countH > len(H) // 2:
    #                 leaderH = H[i]
    #     else:
    #         leaderH = H[0]
    #     if s < len(A):
    #         T.sort()
    #         for i in range(len(T)):
    #             if T[i] != T[i - 1]:
    #                 countT = 1
    #             else:
    #                 countT += 1
    #             if countT > len(T) // 2:
    #                 leaderT = T[i]
    #     else:
    #         leaderT = T[s-1]
    #     if leaderH == leaderT:
    #         equi_count += 1
    # return equi_count
    count = 1
    B = A.copy()
    B.sort()
    leader = -1
    n = 0
    for i in range(len(B)):
        if B[i] != B[i - 1]:
            count = 1
        else:
            count += 1
        if count > len(B) // 2:
            leader = B[i]
            break
    for i in range(len(A)):
        if A[i] == leader:
            n += 1
    eql = 0
    c = 0
    for i in range(len(A)):
        if A[i] == leader:
            c += 1
        if(i+1<2*c and len(A)-i-1<2*(n-c)):
            eql += 1
    return eql

A = [4, 3, 4, 4, 4, 2]
print(solution(A))
