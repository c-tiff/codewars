def save(sizes, hd): 
    i = 0
    count = 0
    for x in sizes:
        i += x
        if i <= hd:
            count += 1
    return count