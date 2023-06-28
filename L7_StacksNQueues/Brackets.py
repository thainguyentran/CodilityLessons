def solution(S):
    if len(S) == 0:
        return 1
    if len(S) == 1 or len(S) % 2 != 0:
        return 0
    parentheses = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for i in S:
        if i in parentheses.keys():
            stack.append(i)
        if i in parentheses.values():
            if stack:
                left = stack.pop()
                if parentheses[left] != i:
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:
        return 1

# S = '{[()()]}'
# S = '([)()]'
# S = ''
S = '()(()()(((()())(()()))'
print(solution(S))
