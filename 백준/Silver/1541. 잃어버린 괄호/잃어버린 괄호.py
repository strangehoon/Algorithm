S = input()

tem = ''
total = 0
flag = False
for i in range(len(S)):
    if S[i] != '+' and S[i] != '-':
        tem += S[i]
    # 괄호 X
    elif flag == False:
        if S[i] == '-':
            flag = True
        total += int(tem)
        tem = ''
    # 괄호 O
    elif flag == True:
        total -= int(tem)
        tem = ''
# 마지막 숫자 계산
if flag == False:
    total += int(tem)
else:
    total -= int(tem)
print(total)