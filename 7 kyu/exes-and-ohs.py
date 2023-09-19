def xo(s):
    s_list = list(s.lower())
    x = s_list.count("x")
    o = s_list.count("o")
    if x == o:
        return True
    else:
        return False