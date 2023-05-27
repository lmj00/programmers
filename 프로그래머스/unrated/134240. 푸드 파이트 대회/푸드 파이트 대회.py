def solution(food):
    
    result = ''
    
    for idx, f in enumerate(food):
        f = f // 2
        result += str(idx) * f    
        
    return result + '0' + result[::-1]