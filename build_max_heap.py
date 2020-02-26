from max_heapify import max_heapify
def build_max_heap(heap):
    heap_size = len(heap) - 1
    for i in range(heap_size // 2, 0, -1):
        max_heapify(heap, heap_size, i)

if __name__ == "__main__":
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print("Before build heap", heap)
    build_max_heap(heap)
    print("After building heap", heap)