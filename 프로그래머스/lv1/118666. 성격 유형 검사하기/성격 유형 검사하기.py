def solution(survey, choices):

    result = ''
    score = '3210123'
    dic = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    for idx, s in enumerate(survey):
        c = choices[idx] - 1
        if c < 3:
            dic[s[0]] += int(score[c]) 
        elif c > 3:
            dic[s[1]] += int(score[c])
    
    result += 'T' if dic['R'] <+dic['T'] else 'R'
    result += 'F' if dic['C'] < dic['F'] else 'C'
    result += 'M' if dic['J'] < dic['M'] else 'J'
    result += 'N' if dic['A'] < dic['N'] else 'A'
        
    return result