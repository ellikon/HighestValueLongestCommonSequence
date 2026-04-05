values = {
    "a": 2,
    "b": 4,
    "c": 5
}

A = "aacb"
B = "caab"


def OPT(i, j):
    if i < 0 or j < 0:
        return 0

    if A[i] == B[j]:
        return values[A[i]] + OPT(i - 1, j - 1)
    else:
        return max(OPT(i - 1, j), OPT(i, j - 1))


print(OPT(len(A) - 1, len(B) - 1))
