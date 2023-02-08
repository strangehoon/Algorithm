A = int(input())
B = int(input())
C = int(input())
data = map(int, list(str(A*B*C)))
result = [0]*10
for i in data:
    result[int(i)] += 1
for i in result:
    print(i)