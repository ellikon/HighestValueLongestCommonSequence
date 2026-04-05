values = {
    "a": 2,
    "b": 4,
    "c": 5
}

A = "aacb"
B = "caab"

M = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            M[i][j] = values[A[i - 1]] + M[i - 1][j - 1]
        else:
            M[i][j] = max(M[i - 1][j], M[i][j - 1])

highest_value = M[len(A)][len(B)]

longest_sequence = " " * highest_value

print(M)
print(highest_value)
