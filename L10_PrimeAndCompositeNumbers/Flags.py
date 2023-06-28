def solution(A):
    peaks = []
    if len(A) < 3:
        return 0
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
    if not peaks:
        return 0
    elif peaks == 1:
        return 1
    flags_count = 1
    maxFlags = 0
    for k in range(min(len(peaks), int(len(A) ** 0.5)) + 1, 0, -1):
        lastFlag = 0
        for i in range(1, len(peaks)):
            if (peaks[i] - peaks[lastFlag]) >= k > flags_count:
                flags_count += 1
                lastFlag = i
        if flags_count < maxFlags:
            return maxFlags
        elif maxFlags < flags_count:
            maxFlags = flags_count
    return maxFlags


A = [1, 2, 3, 1, 5, 3, 10, 4, 5, 2, 5, 6, 3, 4, 6, 4, 5, 8, 9, 2, 6]
print(solution(A))
