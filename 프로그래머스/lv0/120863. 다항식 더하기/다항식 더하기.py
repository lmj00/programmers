def solution(polynomial):
    a = 0
    b = 0

    polynomial = polynomial.split('+')
    
    for i in polynomial:
        i = i.strip() 
        
        if 'x' in i:
            if i == 'x':
                a += 1
            else:
                a += int(i[:-1])

        else:
            b += int(i)
    
    if a == 1:
        a = ''
    
    if a == 0:
        return str(b)
    elif b == 0:
        return str(a) + 'x'
    else:
        return str(a) + 'x + ' + str(b)
        
    
