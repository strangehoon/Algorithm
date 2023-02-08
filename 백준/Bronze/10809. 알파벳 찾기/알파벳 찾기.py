data = list(input())
alpha = [-1]*26
for i in range(len(data)):
    ascii = ord(data[i]) - ord('a')
    if alpha[ascii] == -1:
        alpha[ascii] = i

for i in alpha:
    print(i, end=' ')