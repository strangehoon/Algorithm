import sys
N = int(input())
house_list = []
for i in range(N):
    house_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    house_list[i][0] = min(house_list[i-1][1], house_list[i-1][2]) + house_list[i][0]
    house_list[i][1] = min(house_list[i-1][0], house_list[i-1][2]) + house_list[i][1]
    house_list[i][2] = min(house_list[i-1][0], house_list[i-1][1]) + house_list[i][2]
print(min(house_list[N-1][0], house_list[N-1][1], house_list[N-1][2]))