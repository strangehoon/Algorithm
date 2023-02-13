str = list(input())
new = []
for i in str:
    if i.isupper():
        new.append(i.lower())
    elif i.islower():
        new.append(i.upper())

print(''.join(new))