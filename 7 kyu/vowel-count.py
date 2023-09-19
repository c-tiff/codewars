def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    count = 0
    for x in vowels:
            count += sentence.count(x)
    return count