def solution(quiz):
    
    for i, q in enumerate(quiz):
        v = q.split("=")
        
        if eval(v[0]) == int(v[1]):
            quiz[i] = 'O'
        else:
            quiz[i] = 'X'
            
    
    return quiz