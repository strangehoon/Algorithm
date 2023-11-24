def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    INF = int(1e9)
    for a,b,_,_,_ in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            for a,b,c,d,e in problems:
                if i >= a and j >= b:
                    di = min(i+c, max_alp)
                    dj = min(j+d, max_cop)
                    dp[di][dj] = min(dp[di][dj], dp[i][j] + e)
    return dp[max_alp][max_cop]