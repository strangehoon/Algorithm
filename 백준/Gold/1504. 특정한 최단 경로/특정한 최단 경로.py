import heapq
import sys
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for i in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
result1 = 0
result2 = 0
def dij(s, a, b):
    global result1, result2
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    result1 += distance[a]
    result2 += distance[b]

dij(1, v1, v2)
dij(v1, v2, N)
dij(v2, N, v1)

if result1 >= INF and result2 >= INF:
    print(-1)
else:
    print(min(result1, result2))