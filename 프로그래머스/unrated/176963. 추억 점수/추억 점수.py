def solution(name, yearning, photo):
    
    result = []
    dic = {}
    
    for idx, n in enumerate(name):
        if n not in dic:
            dic[n] = yearning[idx]

            
    for p in photo:
        value = 0
        
        for name in p:
            if name in dic:
                value += dic[name]
        
        result.append(value)
    
    return result