import re
# ok code:
def spin_words(sentence):
    list = sentence.split(" ")
    return " ".join([x[::-1] if len(x)>=5 else x for x in list])
# kind of buggy:
def spin_words(sentence):
    list = sentence.split(" ")
    for x in list:
        if len(x)>=5:
            sentence = re.sub(x, x[::-1], sentence)
    return sentence