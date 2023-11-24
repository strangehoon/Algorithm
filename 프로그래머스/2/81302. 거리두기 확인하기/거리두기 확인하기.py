def solution(places):
    answer = []
    for i in range(5):
        place = places[i]
        graph = []
        flag = 1
        for j in range(5):
            graph.append(list(place[j]))
        for x in range(5):
            for y in range(5):
                if graph[x][y] == 'P':
                    flag = check(graph,x,y)
                if flag == 0:
                    break
            if flag == 0:
                break
        answer.append(flag)
    return answer
def check(graph,x,y):
    # 북, 동, 남, 서,
    dx1 = [-1, 0, 1, 0]
    dy1 = [0, 1, 0, -1]
    # 북동, 남동, 남서, 북서
    dx2 = [-1, 1, 1, -1]
    dy2 = [1, 1, -1,-1]
    # 북북, 동동, 남남, 서서
    dx3 = [-2, 0, 2, 0]
    dy3 = [0, 2, 0, -2]

    # [동,서,남,북] 체크
    for i in range(4):
        dx = x+dx1[i]
        dy = y+dy1[i]
        if 0<=dx<5 and 0<=dy<5:
            if graph[dx][dy] == 'P':
                return 0
    # [북동,남동,남서,북서] 체크
    for i in range(4):
        dx = x+dx2[i]
        dy = y+dy2[i]
        if 0<=dx<5 and 0<=dy<5:
            if graph[dx][dy]=='P':
                if graph[x+dx1[i%4]][y+dy1[i%4]] == 'O' or graph[x+dx1[(i+1)%4]][y+dy1[(i+1)%4]]== 'O':
                    return 0
    # [북북, 동동, 남남, 서서] 체크
    for i in range(4):
        dx = x+dx3[i]
        dy = y+dy3[i]
        if 0<=dx<5 and 0<=dy<5:
            if graph[dx][dy] =='P' and graph[x+dx1[i%4]][y+dy1[i%4]] =='O':
                return 0
    return 1