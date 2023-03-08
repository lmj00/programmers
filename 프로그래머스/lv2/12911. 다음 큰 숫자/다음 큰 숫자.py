def solution(n):
    
    nn = n + 1
    
    while True:
        if bin(n).count('1') == bin(nn).count('1'):
            return nn
            
        nn += 1