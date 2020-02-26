def left(i):
    return i * 2
def right(i):
    return i * 2 + 1
def parent(i):
    return i // 2

def is_max_heap(H):
    n = len(H) - 1
    
    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
    return True

if __name__ == "__main__":
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(is_max_heap(H))
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 4]
    print(is_max_heap(H))
    H = [None, 1, 2, 3]
    print(is_max_heap(H))
    H = [None, 2, 1, 3]
    print(is_max_heap(H))
    H = [None, 3, 1, 2]
    print(is_max_heap(H))
    H = [None, 3, 1, 2]
    print(is_max_heap(H))