def solution(A):
    N = len(A)
    if N == 0:
        return 0
    # positive values
    S = [0] * N
    # negative values
    E = [0] * N

    # PV plus 1
    CS = [0] * N
    # NV plus 1
    CE = [0] * N

    # Sum of previous value array
    CCS = [0] * N
    CCE = [0] * N
    for i in range(N):
        S[i] = i - A[i] if i - A[i] > 0 else 0
        E[i] = i + A[i] if i + A[i] < N-1 else N-1
        CS[S[i]] += 1
        CE[E[i]] += 1
    CCS[0] = CS[0]
    CCE[0] = CE[0]
    for i in range(1, N):
        CCS[i] = CS[i] + CCS[i - 1]
        CCE[i] = CE[i] + CCE[i - 1]

    tot = 0
    for i in range(N):
        if i == 0:
            tot += (CCS[i] - CS[i]) * CS[i] + CS[i] * (CS[i] - 1)//2
        else:
            tot += (CCS[i] - CCE[i-1] - CS[i]) * CS[i] + CS[i] * (CS[i] - 1) // 2
    if tot > 10000000:
        return -1
    return tot


A = [1, 5, 2, 1, 4, 0]
print(solution(A))
