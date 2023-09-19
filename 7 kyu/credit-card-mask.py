def maskify(cc):
    cc_list = list(cc)
    str=""
    if len(cc)>4:
        n = len(cc)-4
        cc_list[0:n] = ["#"*n]
        for x in cc_list:
            str += x
        return str
    else:
        return cc