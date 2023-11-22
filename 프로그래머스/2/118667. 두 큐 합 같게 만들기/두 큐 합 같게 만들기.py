from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    count = 0
    n = len(q1)
    sum1 = sum(q1)
    sum2 = sum(q2)
    while not (len(q1)==0 or len(q2)==0):
        if count > 3*n:
            return -1
        if sum1==sum2:
            return count
        if sum1>sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x
        count+=1
    return -1