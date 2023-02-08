n = int(input())
for i in range(n):
    data = list(input())
    sum = 0
    index = 0
    for j in range(len(data)):
        if data[j] == 'O':
            index += 1
            sum += index
        else:
            index = 0
    print(sum)