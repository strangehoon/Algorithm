n = int(input())
data = []
for i in range(n):
    data.append(input())
alpha = [0] * 26
for i in data:
    length = len(i)
    x = 1
    for j in range(length-1, -1, -1):
        alpha[ord(i[j]) - ord('A')] += x
        x *= 10

alpha.sort(reverse=True)
num = 9
result = 0
for i in alpha:
    result += i*num
    num -= 1
print(result)