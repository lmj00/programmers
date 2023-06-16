def solution(today, terms, privacies):
    result = []
    dic = {}
    ts = today.split('.')

    for t in terms:
        ts = t.split(' ')
        dic[ts[0]] = ts[1]

    for idx, pri in enumerate(privacies):
        ps = pri.split(' ')
        ps_date = ps[0].split('.')
        
        year = int(ps_date[0])
        month = int(ps_date[1]) + int(dic[ps[1]])
        day = ps_date[2]
        
        while month > 12:
            year += 1 
            month -= 12

        if today >= '.'.join([str(year), str(month).zfill(2), day]):
            result.append(idx + 1)
            
    return result