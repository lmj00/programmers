def solution(s):
    result = 0
    str1 = ''
    str2 = ''
    
    for i in s:
        if str1 == '':
            str1 = i
            continue
            
        if i in str1:
            str1 += i
        else:
            if str2 == '':    
                str2 = i
            else:
                str2 += i
            
        if len(str1) == len(str2):
            result += 1
            str1 = ''
            str2 = ''
    
    if 0 < len(str1) or 0 < len(str2):
        result += 1
        
    return result
