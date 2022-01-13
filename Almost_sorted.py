A = [3, 2, 6, 5, 4]
size =2

def sort_k(arr: list, n: int, k: int):
    """
    :param arr: input array
    :param n: length of the array
    :param k: max distance, which every
     element is away from its target position.
    :return: None
    """
    # List of first k+1 items
    heap = arr[:k + 1]
 
    # using heapify to convert list
    # into heap(or min heap)
    heapify(heap)
 
    # "rem_elmnts_index" is index for remaining
    # elements in arr and "target_index" is
    # target index of for current minimum element
    # in Min Heap "heap".
    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1
 
    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1
 


print sort_partially_sorted([3, 2, 6, 5, 4], 2)