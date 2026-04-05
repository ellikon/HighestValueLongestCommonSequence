values = {
    "a": 2,
    "b": 4,
    "c": 5
}

A = "aacb"
B = "caab"
def HVLCS(A,B, values):
    M = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                M[i][j] = max(values[A[i - 1]] + M[i - 1][j - 1],
                              M[i - 1][j], M[i][j - 1])
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1])

    return M, M[len(A)][len(B)]




def find_sequence(A, B, values, M):
    i, j = len(A), len(B)
    longest_sequence = ""
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            longest_sequence = A[i - 1] + longest_sequence
            i -= 1
            j -= 1
        elif M[i - 1][j] == M[i][j]:
            i -= 1
        elif M[i][j - 1] == M[i][j]:
            j -= 1

    return longest_sequence
M, highest_value = HVLCS(A,B,values)
longest_sequence = find_sequence(A,B,values, M)

print(highest_value)
print(longest_sequence)
