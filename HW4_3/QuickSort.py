def qsortIter(x, l, r):
    i = l
    j = r
    p = x[int(l + (r - l) / 2)] 
    while i <= j:
        while x[i] < p: i += 1
        while x[j] > p: j -= 1
        if i <= j: 
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
    if l < j: 
        qsortIter(x, l, j)
    if i < r: 
        qsortIter(x, i, r)
    return x
