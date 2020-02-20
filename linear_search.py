def linear_search(L, x):
    '''
    input: 
    L: list of items
    x: item to search
    output:
    i: index of item if found else -1
    '''
    n = len(L)
    for i in range(n):
        if L[i] == x:
            return i
    return -1
