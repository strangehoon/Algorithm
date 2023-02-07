data = list(map(int, input().split()))
sum = 0
for i in data:
    sum += pow(i, 2)
print(sum % 10)