def solution(A):
    goEast = 0 #cars going east
    pairs = 0 #pairs of passing cars
    for i in A:
        if i == 1:
            pairs += goEast
        else:
            goEast += 1
    if pairs > 1000000000:
        return -1
    else:
        return pairs

A = [0,1,0,1,1]
print(solution(A))