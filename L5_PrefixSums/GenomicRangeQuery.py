# def Solution(S,P,Q):
#     replacements = [("A", "1"), ("C", "2"), ("G", "3"), ("T", "4")]
#     for a, b in replacements:
#         S = S.replace(a, b)
#     qr = len(P)
#     slen = len(S)
#     result = [] * qr
#     for k in range(qr):
#         if Q[k] == P[k]:
#             result.append(int(S[P[k]]))
#         else:
#
#             if Q[k] == slen - 1:
#                 sub = list(map(int, S[P[k]:]))
#             else:
#                 sub = list(map(int, S[P[k]:Q[k + 1]]))
#             result.append(min(sub))
#     return result

def solution(S, P, Q):
    """Solution method implementation."""
    # initialization of variables
    factors = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }
    result = []
    count_states = [[0, 0, 0, 0]]
    # build counter states timeline
    for i, nucleotide in enumerate(S):
        count_states.append(list(count_states[i]))
        count_states[i + 1][factors[nucleotide] - 1] += 1
    # main query processing loop
    for i, _ in enumerate(Q):

        # query substring is of length 1
        if P[i] == Q[i]:
            result.append(factors[S[P[i]]])

        else:

            # get counter states before and after
            state_after_end = count_states[Q[i] + 1]
            state_before_beg = count_states[P[i]]
            # find minimum impact nucleotide in query substring
            for j in range(4):
                if state_after_end[j] > state_before_beg[j]:
                    result.append(j + 1)
                    break

    return result

S = "ACGTATCCTG"
P = [2,5,0]
Q = [3,5,9]
#print(Solution(S, P, Q))
print(solution(S, P, Q))
