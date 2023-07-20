n = int(input())
data = list(map(int, input().split()))

data.sort()

# 홀수
if len(data) % 2 != 0:
    print(data[len(data) // 2])

# 짝수
else:
    print(data[len(data) // 2 -1])