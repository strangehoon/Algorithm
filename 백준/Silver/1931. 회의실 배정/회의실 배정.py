import sys
N = int(input())
data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort(key=lambda x: (x[1],x[0]))
first = data[0]
count = 1
for i in range(1, N):
    if first[1] <= data[i][0]:
        first = data[i]
        count += 1
print(count)
