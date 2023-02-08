A, B = map(int, input().split())

sumA = 0
sumB = 0
param = 100
for i in range(3):
    sumA += A % 10 * param
    sumB += B % 10 * param
    A //= 10
    B //= 10
    param //= 10

if sumA > sumB:
    print(sumA)
else:
    print(sumB)