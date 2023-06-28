# right rotation i - k
# left rotation i + k
def solution(A, K):
    new_num = []
    for i in range(len(A)):
        pos = (i - K) % len(A)
        new_num.append(A[pos])
    return new_num
