# A non-empty zero-indexed array A consisting of N integers is given.
# Array A represents numbers on a tape.
# Any integer P, such that 0 < P < N,
# splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
# The difference between the two parts is the value of:
# |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

def solution(A):
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        #right_sum = s - left_sum
        # difference = right_sum - left_sum
        # so
        # difference = s - left_sum - left_sum
        # or
        # difference = s - 2 * left_sum
        m = min(abs(s - 2 * left_sum), m)
    return m

A = [3, 1, 2, 4, 3]
print(solution(A))
