ch = input()
alpha = [0]*26
for i in range(len(ch)):
    ascii = ord(ch[i])
    if 'A' <= ch[i] <= 'Z':
        alpha[ord(ch[i])-ord('A')] += 1
    else:
        alpha[ord(ch[i])-ord('a')] += 1

if alpha.count(max(alpha)) > 1:
    print('?')
else:
    print(chr(alpha.index(max(alpha)) + 65))