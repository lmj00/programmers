def solution(s):
    
    ls = []
    
    for i in s:
        if len(ls) != 0:
            if ls[-1] == i:
                del ls[-1]  
            else:
                ls.append(i)
        else:
            ls.append(i)

    return 1 if len(ls) == 0 else 0