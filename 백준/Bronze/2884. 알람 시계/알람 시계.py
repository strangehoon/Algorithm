A, B = map(int, input().split())
if A ==0 and B < 45:
    print(23, B+60-45)
elif B < 45:
    print(A-1, B+60-45)
else:
    print(A, B-45)