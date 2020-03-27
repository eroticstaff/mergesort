def recursive(fnumber, snumber):
    str_fnumber = str(fnumber)
    str_snumber = str(snumber)
    n = len(str_fnumber)
    if n >= 2:
        a = int(str_fnumber[0:n // 2])
        b = int(str_fnumber[n // 2:n])
        c = int(str_snumber[0:n // 2])
        d = int(str_snumber[n // 2:n])
        p = a + b
        q = c + d
        ac = recursive(a, c)
        bd = recursive(b, d)
        pq = recursive(p, q)
        adbc = pq - ac - bd
        res = 10 ** n * ac + 10 ** (n // 2) * adbc + bd
        return res
    else:
        res = int(fnumber) * int(snumber)
        return res


# a = int(input("a>>"))
# b = int(input("b>>"))
a = 15
b = 25
res = recursive(a, b)
print(a, "x", b, "=", res)
