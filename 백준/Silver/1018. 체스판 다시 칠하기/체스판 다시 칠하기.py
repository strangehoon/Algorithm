n ,m = map(int , input().split())
d_list = []
for i in range(n):
    d_list.append(list(input()))

for i in range(0, n-7):
    for j in range(0, m-7):
        b_case = 0
        w_case = 0
        for x in range(8):
            for y in range(8):
                if (i+x)%2==0 and (j+y)%2==0:
                    if d_list[i+x][j+y] == 'B':
                        w_case += 1
                    elif d_list[i+x][j+y] == 'W':
                        b_case += 1
                elif (i+x)%2 == 1 and (j+y)%2==1:
                    if  d_list[i+x][j+y] == 'B':
                        w_case += 1
                    elif  d_list[i+x][j+y] == 'W':
                        b_case += 1
                else:
                    if d_list[i+x][j+y] == 'W':
                        w_case += 1
                    elif d_list[i+x][j+y] == 'B':
                        b_case += 1

        if i ==0 and j ==0:
            min_count = min(w_case, b_case)
        else:
            if min_count > min(w_case, b_case):
                min_count = min(w_case, b_case)
print(min_count)