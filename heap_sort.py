from build_max_heap import build_max_heap
from max_heapify import max_heapify
def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1
    for i in range(heap_size, 1, -1):
        heap[1] , heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)
if __name__ == "__main__":
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print("Before sorting", heap)
    heap_sort(heap)
    print("After sorting", heap)