def solution(cacheSize, cities):
    
    time = 0
    ls = []
    
    for city in cities:
        city = city.lower()
        
        if city in ls and cacheSize != 0:
            ls.remove(city)
            time += 1
        else:
            if len(ls) == cacheSize != 0:
                del ls[0]     
            time += 5
            
        ls.append(city)
        
    return time