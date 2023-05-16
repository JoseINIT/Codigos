def enteros(a,b,c):
    d=[a,b,c]
    if d>15:
        return  "El numero mayor es:",max((d))
    elif d<10:
        return "El numero mayor es:",min((d))
    elif d>=10 and d<=15:
        d.sort()
        return d[1]