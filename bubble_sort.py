def bubble_sort(L):
    '''
    input: 
    L list of items
    '''
    n = len(L)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j+1], L[j]
if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print("Before Sort:", L)
    bubble_sort(L)
    print("After Sort:",L)