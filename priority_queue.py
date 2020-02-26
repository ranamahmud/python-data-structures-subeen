from max_heapify import max_heapify

def left(i):
    return i * 2
def right(i):
    return i * 2 + 1
def parent(i):
    return i // 2
def get_maximum(heap):
    return heap[1]

def extract_max(heap, heap_size):
    max_item = heap[1]
    heap[1] = heap[heap_size]
    heap_size -= 1
    max_heapify(heap, heap_size, 1)
    return max_item
def insert_node(heap, heap_size, node):
    heap_size += 1
    heap[heap_size] = node
    i = heap_size
    
    while i > 1 and heap[i] > heap[parent(i)]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)
        
    return heap_size

if __name__ == "__main__":
    h = [None,19, 10, 17, 5, 7, 12, 1, 2, 3]
    print(get_maximum(h))
    print(extract_max(h, len(h)-1))
    print(h)
    