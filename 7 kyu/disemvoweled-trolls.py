import re
def disemvowel(string_):
    newstring = re.sub("a|i|u|e|o","",string_,flags=re.IGNORECASE)
    return  newstring