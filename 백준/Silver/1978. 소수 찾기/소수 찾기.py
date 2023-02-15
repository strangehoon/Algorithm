import math
n = int(input())

data = map(int, input().split())
answer = 0

for i in data:
    answer += 1
    if i == 1:
        answer -= 1
    for j in range(2, int(math.sqrt(i))+1, 1):
        if i % j ==0:
            answer -= 1
            break
print(answer)