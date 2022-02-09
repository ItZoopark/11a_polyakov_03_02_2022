def polyakov_bad():
    k = 12
    while True:
        k -= 1
        x = 1
        y = x
        kc = k
        while kc < 13:
            kc += 1
            if kc == 7:
                t = 0
            else:
                t = x + y
            x = y
            y = t
        if kc == 13 and x == 25:
            return k


# print(polyakov_bad())
def polyakov_4112():
    count = 0
    for x in range(16 ** 5, 16 ** 6):
        L, M = 0, 0
        while x > 0:
            L = L + 1
            if x % 16 % 2 == 0:
                M = M + 1
            else:
                M = M - 1
            x = x // 16
        if L == 6 and M == 0:
            count += 1
    print(count)


# polyakov_4112()

def polyakov_1():
    T = 0
    while True:
        T += 1
        c = 0
        N = 0
        d = 5
        Tc = T
        cc = c
        Nc = N
        while Nc != 300:
            Nc = Nc + Tc
            Tc = Tc + d
            cc = cc + 1
            if Nc > 300:
                break
        if cc % 2 != 0:
            cc = cc + d
        if cc == 8:
            print(T)
            return

# polyakov_1()

def sum(x):
    s = 0
    while x != 0:
        s += x%10
        x //= 10
    return s

def polyakov_2938():
    x = 0
    while True:
        x += 1
        xc = x
        L = 0
        Lc = L
        M = 1
        Mc = M
        while xc > 0:
            Lc = xc % 8 * Mc + Lc
            xc = xc // 8
            Mc = Mc * 10
        if sum(Lc) == 15:
            print(x)
            return

polyakov_2938()









