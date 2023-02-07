def solution(arr):
    
    v = ''
    ls = []
    
    for i in arr:
        if v != i:
            v = i
            ls.append(v)
            
    return ls