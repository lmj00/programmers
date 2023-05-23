from collections import deque

def solution(ingredient):
    q = deque()
    result = 0

    for i in ingredient:
        q.append(i)

        if len(q) >= 4:
            if q[-1] == 1 == q[-4] and q[-2] == 3 and q[-3] == 2:
                for i in range(4):
                    q.pop()
                    
                result += 1
                
    return result