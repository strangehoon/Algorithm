n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

for i in range(n-2, -1, -1):
    for j in range(len(tri[i])):
        tri[i][j] = max(tri[i+1][j] + tri[i][j], tri[i+1][j+1] + tri[i][j])

print(tri[0][0])
