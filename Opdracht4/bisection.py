def findRoot(f, a, b, epsilon):
    m = (a+b)/2.0
    print(m)
    if m == 0:
        return m
    elif b-a <= epsilon and b-a >= -epsilon:
        return m
    if (f(a) > 0 and f(m) <0) or (f(a) < 0 and f(m) > 0):
        return findRoot(f, a, m, epsilon)
    else:
        return findRoot(f, m, b,epsilon)

