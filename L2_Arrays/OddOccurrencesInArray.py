A = [9, 3, 9, 3, 9, 7, 9, 7, 9]

# this version is too slow for big data(big random test n=999,999, multiple repetitions)
def solution(A):
    set_ofA = set(A)
    for v in set_ofA:
        count = A.count(v)
        if count % 2:
            return v
    return 0

# We can solve this problem in a single traversal of the array and constant space.
# The idea is to use the XOR operator.
# We know that if we XOR a number with itself an odd number of times, the result is the number itself;
# otherwise, if we XOR a number an even number of times with itself, the result is 0.
# Also, the XOR of a number with 0 is always the number itself.
# ^ is the XOR operator in python
# print bitwise XOR operation
# print("a ^ b =", a ^ b)
def sol(A):
    xor = 0
    for i in A:
        xor = xor ^ i

    return xor

print(solution(A))
print(sol(A))

