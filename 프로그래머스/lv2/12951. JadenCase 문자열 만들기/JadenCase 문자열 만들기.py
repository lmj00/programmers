def solution(s):
    
    result = ''
    ss = ''
    
    for i, v in enumerate(s):
        ss += v
        
        if v == ' ' or i == len(s) - 1:
            result += ss.capitalize()
            ss = ''
        
    return result