import sys
N, C = map(int, input().split())
data = []
for _ in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()

result = []
def binary_search(start, end):
    if start > end:
        return
    target = (start + end)//2
    count = 1
    x = data[0]
    for i in range(1, len(data)):
        if x + target <= data[i]:
            x = data[i]
            count += 1
    if count < C:
        binary_search(start, target-1)
    else:
        result.append(target)
        binary_search(target+1, end)

binary_search(1, data[-1] - data[0])
print(result[-1])