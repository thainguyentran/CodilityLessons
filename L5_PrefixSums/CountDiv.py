def Solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K


A = 6
B = 11
K = 2
print(Solution(A, B, K))