def solution(n):
    result = [1, 1]
    
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
            
    return result[-1] % 1234567