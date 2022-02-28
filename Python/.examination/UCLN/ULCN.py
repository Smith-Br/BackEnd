with open("UCLN.INP") as fi:
    m, n = map(int, fi.readline().split())

def ucln(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
out = ucn(m, n)

with open("UCLN.OUT", "w") as fo:
    fo.write(str(out))