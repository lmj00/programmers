def solution(n, arr1, arr2):
    
    result = []
    
    for i in range(len(arr1)):
        s = ''
        b = bin(arr1[i] | arr2[i])
        
        if len(b) < n + 2:
            s += ' ' * (n + 2 - len(b))
        
        for j in range(2, len(b)):
            if b[j] == '1':
                s += '#'
            else:
                s += ' '
                
        result.append(s)
        
    return result