def duplicate_count(text):
    text1 = text.lower()
    set = {x for x in text1 if text1.count(x)>1}
    count = 0
    for x in set:
        count += 1
    return count