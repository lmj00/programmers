def solution(n, words):
    ls = [words[0]]
    
    for i in range(1, len(words)):
        if words[i] not in ls and ls[-1][-1] == words[i][0] and len(words[i]) > 1:
            ls.append(words[i])
        else:
            break
            
    if len(ls) == len(words):
        return [0, 0]
    
    return [len(ls) % n + 1, len(ls) // n + 1]