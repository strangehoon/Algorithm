N, S = map(int, input().split())
data = list(map(int, input().split()))
visited = [False] * N
result = 0

def dfs(index, sum, count):
    global result
    # 종료 조건
    if index >= N:
        if sum == S and count > 0:
            result += 1
        return
    # 하부함수 호출
    dfs(index+1, sum + data[index], count+1)
    dfs(index+1, sum, count)

dfs(0, 0, 0)
print(result)