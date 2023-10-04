import sys
from collections import defaultdict

num_data = defaultdict(int)
n = 0
while True:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    num_data[word] += 1
    n += 1

num_data = sorted(num_data.items())
for key, value in num_data:
    value = value/n*100
    print(key, format(value, ".4f"))