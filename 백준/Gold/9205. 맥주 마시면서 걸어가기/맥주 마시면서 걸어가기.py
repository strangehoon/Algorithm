from collections import deque
t = int(input())
result = []
def bfs(house_x, house_y, festival_x, festival_y):
    queue = deque([(house_x, house_y)])
    while queue:
        current_x, current_y = queue.popleft()
        if abs(festival_x-current_x) + abs(festival_y-current_y) <= 1000:
            result.append("happy")
            return
        for i in range(n):
            store_x, store_y = store_list[i][0], store_list[i][1]
            if not v_list[i]:
                if abs(store_x-current_x) + abs(store_y-current_y) <= 1000:
                    v_list[i] = True
                    queue.append((store_x, store_y))
    result.append("sad")

for _ in range(t):
    store_list = []
    n = int(input())
    house_x, house_y = map(int, input().split())
    v_list = [False] * n
    for i in range(n):
        store_x, store_y = map(int, input().split())
        store_list.append((store_x, store_y))
    festival_x, festival_y = map(int, input().split())
    bfs(house_x, house_y,festival_x, festival_y)
for i in result:
    print(i)