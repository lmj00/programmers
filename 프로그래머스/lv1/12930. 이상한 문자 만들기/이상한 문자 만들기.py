def solution(ss):

    result = []
    blank = []
    
    for idx, v in enumerate(ss):
        if v == ' ':
            blank.append(idx)
    
    for word in ss.split():
        for idx, s in enumerate(word):
            if idx % 2 == 0:
                result.append(s.upper())
            else:
                result.append(s.lower())
        
    for idx, v in enumerate(blank):
        result.insert(v, ' ')
        
    return ''.join(result)