import math
m, n = map(int, input().split())

for i in range(m, n+1):
    count = 1
    for j in range(2, (int)(math.sqrt(i))+1):
        if i % j == 0:
            count += 1
            break
    if count == 1 and i != 1:
        print(i)