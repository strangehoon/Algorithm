import sys
n = int(input())

data = []
stack = []
result = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))
cnt = 1
for x in data:
    while(cnt <= n+1):
        if cnt <= x:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        else:
            t = stack.pop()
            if t == x:
                result.append('-')
                break
            else:
                print("NO")
                exit(0)

for i in result:
    print(i)