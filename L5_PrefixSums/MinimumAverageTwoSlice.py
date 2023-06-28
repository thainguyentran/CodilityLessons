def solution(A):
    minavg = 10001
    result = 0
    for i in range(len(A)-1):
        avg = (A[i] + A[i+1])/2
        if avg < minavg:
            minavg = avg
            result = i
        if i < len(A)-2:
            avg = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg < minavg:
                minavg = avg
                result = i
    return result


A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))
