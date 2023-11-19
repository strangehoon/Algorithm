result = []
def dfs(c, l_list, q):
    if c == 6:
        result.append(l_list)
        return
    for i in range(q, s):
        dfs(c+1, l_list + [data[i]],i+1)

while(True):
    data = list(map(int, input().split()))
    # 입력 종료
    if len(data)==1:
        break
    s = data[0]
    data = data[1:]
    dfs(0, [], 0)
    result.append("")
for i in result:
    print(*i)