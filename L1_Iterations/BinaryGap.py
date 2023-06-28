def solution(N):
    # Implement your solution here
    bin_num = bin(N).replace("0b", "")
    i = j = 0
    start = max = 0
    end = start + 1
    for i in range(len(bin_num)):
        if bin_num[i] == '1':
            start = i
    return max


def binaryGap(N):
    B = bin(N).replace('0b', '')
    K = str(B)
    K = list(K)
    Max = 0
    C = 0
    S = 0
    Flag = False
    for i in range(len(K)):
        if K[i] == '1' and C == 0 and Flag is False:
            C = i
            Flag = True
        elif K[i] == '1' and Flag:
            S = i
        if Max < abs(S - C):
            Max = abs(S - C)
            C = S
    return Max

def binary_gap2(N):
    return len(max(format(N, 'b').strip('0').split('1')))

# print(solution(561892))
print(binaryGap(561892))
print(binary_gap2(561892))