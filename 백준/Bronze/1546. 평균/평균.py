N = int(input())
score = list(map(int, input().split()))
max_value = max(score)
total = 0
for i in range(len(score)):
    score[i] = score[i] / max_value * 100
    total += score[i]

average = total/len(score)
print(average)
