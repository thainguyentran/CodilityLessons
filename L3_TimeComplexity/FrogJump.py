
def solution(X, Y, D):
    # Implement your solution here
    distance = Y - X
    count = 0
    if distance <= 0:
        return 0
    else:
        steps = round(distance / D)
        totaldis = steps * D + X
        if totaldis < Y:
            return steps + 1
        else:
            return steps

print(solution(10, 85, 30))