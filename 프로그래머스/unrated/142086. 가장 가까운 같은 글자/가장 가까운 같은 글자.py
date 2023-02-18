def solution(s):
    dic = {}
    ls = []
    
    for i, v in enumerate(s):
        
        if v not in dic:
            ls.append(-1)
        else:
            ls.append(i - dic[v])
        dic[v] = i
            
    return ls