def solution(A):
    N = len(A)
    maxA = max(A)
    #keep track of the occurence of the number in the array
    counts = [0] * (1 + maxA)
    #keep track of the non divisors of the number from 0 to the largest number in the list
    non_divisible = [0] * (1 + maxA)
    #keep track of the number have been checked for non divisors. this one work hand in hand with the list above
    visited = [False] * (1 + maxA)
    #count the occurence
    for number in A:
        counts[number] += 1
    #keep the result in this array
    non_divisors = []
    for number in A:
        if visited[number]:
            non_divisors.append(non_divisible[number])
        else:
            divisors_of_number = 0
            for divisor in range(1, int(number ** 0.5) + 1):
                if number % divisor == 0:
                    divisors_of_number += counts[divisor]
                    other_divisor = int(number / divisor)
                    if other_divisor != divisor:
                        divisors_of_number += counts[other_divisor]
            non_divisors.append(N - divisors_of_number)
            non_divisible[number] = N - divisors_of_number
            visited[number] = True
    return non_divisors