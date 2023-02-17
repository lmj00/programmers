def solution(num, total):
    
    answer = [i for i in range(1, num + 1)]
    
    while sum(answer) != total:
        
        for j in range(len(answer)):
            if sum(answer) > total:
                answer[j] = answer[j] - 1
            else:
                answer[j] = answer[j] + 1
            
    return answer