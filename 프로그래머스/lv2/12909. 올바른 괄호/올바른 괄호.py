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
    
    return True if len(v) == 0 else False 