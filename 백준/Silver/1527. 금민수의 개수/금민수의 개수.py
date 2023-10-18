from collections import deque
A, B = map(int, input().split())

queue1 = deque(['4'])
count = 0
while queue1:
    x = queue1.popleft()
    if A <= int(x) <= B:
        count += 1
    if len(str(x)) > len(str(B)):
        break
    queue1.append(x+'4')
    queue1.append(x+'7')

queue2 = deque(['7'])
while queue2:
    y = queue2.popleft()
    if A <= int(y) <= B:
        count += 1
    if len(str(y)) > len(str(B)):
        break

    queue2.append(y+'4')
    queue2.append(y+'7')

print(count)