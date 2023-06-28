# Find the smallest positive integer that does not occur in a given sequence.

def Solution(A):
    setA = set(A)
    possetA = [i for i in setA if i > 0]
    if 1 not in possetA or not possetA:
        return 1
    else:
        maxA = max(possetA)
        sumofposA = sum(possetA)
        if sumofposA == (maxA * (maxA + 1))//2:
            return maxA + 1
        else:
            return (maxA * (maxA + 1))//2 - sumofposA


A = [1, 3, 6, 4, 1, 2]
print(Solution(A))
print(Solution([1,2,3]))
print(Solution([-1,-3,-5,-1]))