def likes(names):
    singular = " likes this"
    plural = " like this"
    multi = " others like this"
    if len(names)==0:
        return "no one" + singular
    elif len(names)==1:
        return names[0] + singular
    elif len(names)==2:
        return " and ".join(names[0:2]) + plural
    elif len(names)==3:
        return ", ".join(names[0:2]) + " and " + names[2] + plural
    elif len(names)>=4:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + multi