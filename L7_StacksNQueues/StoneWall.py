def Solution(H):
    last = 0
    stone_counter = 0
    S = []
    for i in range(len(H)):
        if H[i] > last:
            last = H[i]
            S.append(H[i])
            stone_counter += 1
        elif H[i] < last:
            while len(S) > 0 and H[i] < S[-1]:
                S.pop()
            if len(S) == 0 or H[i] != S[-1]:
                stone_counter += 1
                S.append(H[i])
            last = H[i]
    return stone_counter

H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(Solution(H))