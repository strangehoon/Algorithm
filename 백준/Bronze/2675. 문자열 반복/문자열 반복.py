N = int(input())
for i in range(N):
    A, B = input().split()
    for i in range(len(B)):
        print(int(A)*B[i], end='')
    print()