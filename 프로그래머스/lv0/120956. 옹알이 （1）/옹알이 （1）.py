def solution(babbling):
    pos_word = ["aya", "ye", "woo", "ma" ]
    result = 0
    
    for i in babbling:
        word_len = 0

        for j in pos_word:
            if j in i:
                word_len += len(j)
        
        if word_len == len(i):
            result += 1
            
    return result