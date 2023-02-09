while(True):
    data = list(input())
    check = 0
    if data == ['0']:
        break
    for i in range(len(data)//2):
        if data[i] != data[len(data)-1-i]:
            print("no")
            check = 1
            break
    if check == 0:
        print("yes")