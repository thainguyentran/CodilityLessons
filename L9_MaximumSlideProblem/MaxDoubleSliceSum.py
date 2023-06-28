def solution(A):
    n = len(A)
    if n <= 3:
        return 0
    LR = n * [0]
    RL = n * [0]

    s = 0
    for i in range(1, n-1):
        s += A[i]
        if s < 0:
            s = 0
        LR[i] = s
    s = 0
    for i in range(n-2, 0, -1):
        s += A[i]
        if s < 0:
            s = 0
        RL[i] = s
    m = 0
    for i in range(0, n-2):
        m = max(m, LR[i]+RL[i+2])
    return m

A = [3, 2, 6, -1, 4, 5, -1, 2]
print(solution(A))
