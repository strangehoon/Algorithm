X = int(input())

data = [0 for _ in range(X+1)]

for i in range(2, X+1):
    data[i] = data[i-1] + 1
    if i % 3 == 0:
        data[i] = min(data[i//3] + 1, data[i])
    if i % 2 ==0:
        data[i] = min(data[i//2] + 1, data[i])

print(data[X])