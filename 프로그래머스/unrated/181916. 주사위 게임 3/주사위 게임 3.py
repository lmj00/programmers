from collections import Counter

def solution(a, b, c, d):
    
    ls = [a, b, c, d]
    c = Counter(ls).most_common()
    
    if c[0][1] == 4:
        return 1111 * c[0][0]
    elif c[0][1] == 3:
        return (10 * c[0][0] + c[1][0]) ** 2
    elif c[0][1] == 2 and c[1][1] == 2:
        return (c[0][0] + c[1][0]) * abs(c[0][0] - c[1][0])
    elif c[0][1] == 2:
        return c[1][0] * c[2][0]
    else:
        return min(ls)