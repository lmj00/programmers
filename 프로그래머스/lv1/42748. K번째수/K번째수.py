def solution(array, commands):

    ls = []
    
    for i in commands:  
        v = sorted(array[i[0] - 1:i[1]])
        ls.append(v[i[2] - 1])
        
    return ls