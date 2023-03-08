def solution(numbers):
    answer = []
    numbers.sort()
    
    for i in range(len(numbers)):
        for j in numbers[i + 1:]:
            answer.append(numbers[i] + j)
            
    return sorted(set(answer))