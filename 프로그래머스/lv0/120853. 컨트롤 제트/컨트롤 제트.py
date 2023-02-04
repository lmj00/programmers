def solution(s):
    
    result = 0
    s = s.split()
    
    for i in s:
        if i == 'Z':
            result -= int(check)  
            continue
        
        result += int(i)
        check = int(i)
    
    return result
