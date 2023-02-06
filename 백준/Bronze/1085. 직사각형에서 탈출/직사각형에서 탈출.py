x, y, w, h = map(int, input().split())

data_x = x if x < w-x else w-x
data_y = y if y < h-y else h-y

print(min(data_x, data_y))