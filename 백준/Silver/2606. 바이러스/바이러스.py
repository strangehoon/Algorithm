from collections import deque
a = int(input())
b = int(input())

graph = [[] for _ in range(a+1)]
result = []
for _ in range(b):
    m, n = map(int, input().split())
    graph[m].append(n)
    graph[n].append(m)

queue = deque([1])
result.append(1)

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if i not in result:
            result.append(i)
            queue.append(i)

print(len(result)-1)