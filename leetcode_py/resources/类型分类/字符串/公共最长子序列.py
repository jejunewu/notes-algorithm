s1,s2 = "1A2C3D4B56","B1D23CA45B6A"

#####################
m, n = len(s1), len(s2)
dp = [[0 for i in range(n+1)] for j in range(m+1)]


for i in range(1, m+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp)

# 输出LCS

ans = ''
i, j = m, n
while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:

        ans+=s1[i - 1]
        i -= 1
        j -= 1
        #continue
    else:
        if dp[i][j - 1] >= dp[i - 1][j]:
            j -= 1
        else:
            i -= 1

print(ans[::-1])
# print(m,n)
# ans = ''
# while m>0 and n>0:
#     if dp[m][n] == dp[m-1][n] or dp[m][n] == dp[m][n-1]:
#         print(1111111)
#         if dp[m][n] == dp[m-1][n]:
#             m -= 1
#         else:
#             n -=1
#
#     elif dp[m][n] == dp[m-1][n]-1 and s1[m-1]==s2[n-1]:
#         m -= 1
#         ans+=s1[m-1]
#     elif dp[m][n] == dp[m][n-1]-1 and s1[m-1]==s2[n-1]:
#         n -= 1
#         ans+=s1[n-1]


def LCS( s1, s2):
    # write code here
    m, n = len(s1), len(s2)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 输出LCS
    ans = ''
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i][j - 1] >= dp[i - 1][j]:
                j -= 1
            else:
                i -= 1
    return -1 if dp[-1][-1] == 0 else ans[::-1]

A = LCS(s1, s2)
print(A)