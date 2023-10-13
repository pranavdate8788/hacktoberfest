def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a table to store the lengths of LCS for subproblems
    L = [[0] * (n + 1) for i in range(m + 1)]

    # Build the L table using dynamic programming
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Read the LCS from the table
    index = L[m][n]
    lcs = [''] * (index + 1)
    lcs[index] = ''

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
result = longest_common_subsequence(X, Y)
print("Longest Common Subsequence:", result)
