def solution(N):
    if N == 1:
        return 1
    factor = []
    i = 1
    while i * i <= N:
        if N % i == 0:
            if N / i != i:
                factor.append(i)
                factor.append(N // i)
            else:
                factor.append(i)
        i += 1
    return len(factor)


N = 5621892
print(solution(N))
