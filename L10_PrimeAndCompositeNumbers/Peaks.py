def solution(A):
    N = len(A)
    if N < 3:
        return 0
    # first find the peaks
    peaks = [False] * N
    for i in range(1, N - 1):
        if A[i - 1] < A[i] and A[i + 1] < A[i]:
            peaks[i] = True
    npeaks = sum(peaks)
    if npeaks == 0:
        return 0

    for jj in range(npeaks, 0, -1):
        # check if the nb of blocks exist
        if N % jj == 0:
            # I have jj blocks with NELEM each
            NELEM = N // jj
            # check if all the sub slices have a peak
            found = True
            for kblock in range(jj):
                # The extreme points of the chunk
                chunk = [kblock * NELEM, (1 + kblock) * NELEM]
                # found one block with no peaks
                if not True in peaks[chunk[0]:chunk[1]]:
                    found = False
                    break
            if found:
                return jj


A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
B = [1, 2, 3, 4, 5, 6]
print(solution(A))