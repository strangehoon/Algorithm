n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    x = len(tri[i])
    for j in range(x):
        first = tri[i+1][j]
        second = tri[i+1][j+1]
        if first > second:
            tri[i][j] = first + tri[i][j]
        else:
            tri[i][j] = second + tri[i][j]
print(tri[0][0])