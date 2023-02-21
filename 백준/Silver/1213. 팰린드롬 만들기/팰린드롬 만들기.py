l = list(input())
s = set(l)

data = []
check = 0
odd = 0
for i in range(len(s)):
    x = s.pop()
    if l.count(x) % 2 == 1:
        check += 1
        odd = x
    for i in range(int(l.count(x)/2)):
        data.append(x)
data.sort()

# 팰린드롬 수 가능 (모든 문자의 개수가 짝수개 혹은 홀수개인 문자의 개수가 1개)
if check <= 1:
    for i in range(len(data)):
        print(data[i], end='')
    # 홀수개인 문자의 개수가 1개
    if check == 1:
        print(odd, end = '')
    for i in range(len(data)):
        print(data[len(data)-1-i], end ='')

# 팰린드롬 수 불가능 (문자의 개수가 홀수개인 문자의 개수가 2개 이상)
else :
    print("I'm Sorry Hansoo")