n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = int(-1e9)
min_value = int(1e9)

def dfs(index, element):
    global max_value, min_value, add, sub, mul, div
    if index == n-1:
        max_value = max(max_value, element)
        min_value = min(min_value, element)
        return

    # case : +
    if add >0:
        add -= 1
        dfs(index+1, element + data[index+1])
        add += 1
    # case : -
    if sub >0:
        sub = sub -1
        dfs(index+1, element - data[index+1])
        sub = sub + 1
    # case : *
    if mul >0:
        mul = mul - 1
        dfs(index+1, element * data[index+1])
        mul = mul +1
    # case : //
    if div >0:
        div = div -1
        dfs(index+1, int(element/data[index+1]))
        div = div +1

dfs(0, data[0])
print(max_value)
print(min_value)