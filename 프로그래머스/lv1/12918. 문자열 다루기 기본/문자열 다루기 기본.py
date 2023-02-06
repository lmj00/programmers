def solution(s):
    v = '0123456789'
    
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i not in v:
                return False
            
        return True
    
    return False