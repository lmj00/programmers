def solution(ss, n):
    result = ''

    for s in ss:
        s = ord(s) 
        
        if 97 <= s <= 122:
            if s + n > 122:
                s = s + n - 122 + 96
            else:
                s += n        
                
        elif 65 <= s <= 90:
            if s + n > 90:
                s = s + n - 90 + 64      
            else:
                s += n        
            
        result += chr(s)
    
    return result