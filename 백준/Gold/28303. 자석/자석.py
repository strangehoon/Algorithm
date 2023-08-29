n, k = map(int, input().split())
data = list(map(int, input().split()))

first_answer = -10e10
min_value = data[0]-k
for i in range(1, n):
    first_answer = max(first_answer, data[i]-(i+1)*k-min_value)
    min_value = min(min_value, data[i]-(i+1)*k)

# n극 s극 바꿔서 생각 -> 리스트 역순 정렬
data.reverse()
second_answer = -10e10
min_value = data[0]-k
for i in range(1, n):
    second_answer = max(second_answer, data[i]-(i+1)*k-min_value)
    min_value = min(min_value, data[i]-(i+1)*k)

print(max(first_answer, second_answer))