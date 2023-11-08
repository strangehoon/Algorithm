N = int(input())

v1 = [False]*(2*N-1)
v2 = [False]*(2*N-1)
v3 = [False]*(2*N-1)
ans = 0
def dfs(x):
    global ans
    if x == N:
        ans += 1
        return
    for y in range(N):
        if not v1[y] and not v2[y - x] and not v3[x + y]:
            v1[y], v2[y - x], v3[x + y] = True, True, True
            dfs(x+1)
            v1[y], v2[y - x], v3[x + y] = False, False, False

dfs(0)
print(ans)