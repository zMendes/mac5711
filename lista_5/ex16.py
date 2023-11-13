def getMaxLucro_init(n, d, p):
    return getMaxLucro(n, d, p, dp, 0)



def getMaxLucro(n, d, p, dp, t):
    without = getMaxLucro(n-1, d, p, dp, t)
    if n < 0:
        return 0
    if d[n] > t:
        with = p[n] + getMaxLucro(n-1, d, p, dp, t-d[n])
    if with == max(with, without):
        dp.append(n)
        return with
    dp.remove(n)
    return without
    
