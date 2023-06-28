# Calculate the values of counters after applying all alternating operations:
# increase counter by 1; set value of all counters to current maximum.

# my solution
def Solution(N, A):
    current_max = 0
    result = [0] * N
    for i in A:
        if i <= N:
            result[i-1] += 1
            current_max = max(result[i-1], current_max)
        elif i > N:
            result = [current_max] * N
    return result

# 88%
def Solution2(N, A):
    maxcount=0
    counter=[maxcount]*N
    can_be_updated = True
    for J in A:
        if J<=N:
            counter[J-1]+=1
            maxcount = max(maxcount,counter[J-1])
            can_be_updated = True
        elif can_be_updated:
                counter = [maxcount]*N
                can_be_updated = False
    return counter


print(Solution(5, [3, 4, 4, 6, 1, 4, 4]))
print(Solution2(5, [3, 4, 4, 6, 1, 4, 4]))