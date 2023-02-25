def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    sum = 0
    
    for i, v in enumerate(A):
        sum += A[i] * B[i]
    
    return sum