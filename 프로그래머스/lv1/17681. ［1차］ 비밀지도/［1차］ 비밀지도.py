def solution(n, arr1, arr2):
    
    ls = [bin(arr1[i] | arr2[i]) for i in range(len(arr1))]
    result = []
    
    for width in ls:
        s = ''
        if len(width) < n + 2:
            s += ' ' * (n + 2 - len(width))
        
        for j in range(2, len(width)):
            if width[j] == '1':
                s += '#'
            else:
                s += ' '
                
        result.append(s)
        
    return result