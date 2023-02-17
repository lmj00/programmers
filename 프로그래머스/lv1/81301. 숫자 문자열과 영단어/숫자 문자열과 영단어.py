def solution(s):
    
    dic = {}
    
    dic['zero'] = '0'
    dic['one'] = '1'
    dic['two'] = '2'
    dic['three'] = '3'
    dic['four'] = '4'
    dic['five'] = '5'
    dic['six'] = '6'
    dic['seven'] = '7'
    dic['eight'] = '8'
    dic['nine'] = '9'
    
    ss = ''
    result = ''
    
    for i in s:
        if i in '0123456789':
            result += i
        else:
            ss += i

            if ss in dic:
                result += dic[ss]
                ss = ''
    
    return int(result)   