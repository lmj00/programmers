def solution(s):
    
    count = 0
    zero = 0
    
    while s != '1':
        ss = ''
        for i in range(s.count('1')):
            ss += '1'
        
        zero += len(s) - len(ss)
        s = bin(len(ss))[2:]
        count += 1
        
    return [count, zero]
        