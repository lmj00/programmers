def solution(s):
    
    v = []
    
    for i in s:
        if i == '(':
            v.append('(')
        else:
            if len(v) == 0:
                return False
            else:
                del v[-1]                
    
    return len(v) == 0 