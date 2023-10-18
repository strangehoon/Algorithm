from collections import deque
A, B = map(int, input().split())

queue = deque(['4','7'])
count = 0
while queue:
    x = queue.popleft()
    if int(x)<=B:
        if A<=int(x):
            count += 1
        queue.append(x+'4')
        queue.append(x+'7')
print(count)