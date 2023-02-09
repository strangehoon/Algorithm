n = int(input())

# 영단어 입력
data = []
for i in range(n):
    data.append(input())

# 오름차순 정렬
data.sort()

# 중복 제거
result = []
for x in data:
    if x not in result:
        result.append(x)

# 글자 순으로 오름차순 정렬
for x in sorted(result, key=lambda alpha:len(alpha)):
    print(x)