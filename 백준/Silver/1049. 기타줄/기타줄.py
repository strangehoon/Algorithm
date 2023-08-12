import sys
N, M = map(int, input().split())
data = []
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    data.append((a,b))

price = 0
x = min(data, key=lambda x:x[0])[0]
y = min(data, key=lambda x:x[1])[1]
# 패키지가 이득인 경우
if x < y*6:
    price += (N//6 * x)
    if x < (N % 6*y):
        price += x
    else:
        price += (N % 6 *y)
# 낱개가 이득인 경우
else:
    price += (N * y)
print(price)
